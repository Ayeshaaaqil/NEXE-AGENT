<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NexeCalc Pro | Universal Math Agent</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script>
        // Tailwind dark mode configuration
        tailwind.config = { darkMode: 'class' }
    </script>
    <style>
        /* Modern Glassmorphism Styles */
        .glass { 
            backdrop-filter: blur(16px); 
            -webkit-backdrop-filter: blur(16px);
        }
        .dark .glass { 
            background: rgba(15, 23, 42, 0.8); 
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .light .glass { 
            background: rgba(255, 255, 255, 0.7); 
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #38bdf8; border-radius: 10px; }
    </style>
</head>
<body class="transition-colors duration-500 min-h-screen flex items-center justify-center p-4 sm:p-6 bg-slate-50 dark:bg-[#020617]">

    <!-- Main Responsive Card -->
    <div class="w-full max-w-[95%] sm:max-w-md glass rounded-[2.5rem] shadow-2xl p-6 sm:p-8 relative overflow-hidden transition-all duration-500">
        
        <!-- Header & Theme Toggle -->
        <header class="flex justify-between items-center mb-8">
            <div>
                <h1 class="text-2xl font-bold dark:text-white text-slate-900 tracking-tight italic">Nexe<span class="text-sky-500">Calc</span></h1>
                <p class="text-[9px] text-sky-500 font-bold uppercase tracking-widest mt-1">Adaptive AI Agent</p>
            </div>
            <div class="flex gap-2">
                <!-- Theme Toggle Button -->
                <button onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:scale-110 transition active:scale-95">
                    <i id="themeIcon" class="fas fa-moon"></i>
                </button>
                <button onclick="clearMemory()" class="p-2 rounded-xl bg-red-100 dark:bg-red-900/20 text-red-600 dark:text-red-400 hover:scale-110 transition active:scale-95">
                    <i class="fas fa-rotate-left"></i>
                </button>
            </div>
        </header>

        <!-- Display Panel -->
        <div class="bg-white/50 dark:bg-black/40 rounded-3xl p-6 mb-6 border border-slate-200 dark:border-slate-800/50 shadow-inner">
            <div id="expView" class="text-right text-[10px] sm:text-xs text-slate-400 font-mono h-4 mb-1"></div>
            <div class="flex justify-between items-center gap-4">
                <button onclick="copyToClipboard()" class="text-slate-400 hover:text-sky-500 active:scale-90 transition">
                    <i id="copyIcon" class="far fa-clone text-lg sm:text-xl"></i>
                </button>
                <div id="resultView" class="text-4xl sm:text-5xl font-mono dark:text-white text-slate-900 truncate">0</div>
            </div>
        </div>

        <!-- Adaptive Input Area -->
        <div class="relative mb-8 group">
            <input id="agentInput" type="text" onkeydown="if(event.key==='Enter') executeAgent()" 
            placeholder="Type: '10% of 500'..." 
            class="w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 pr-14 focus:outline-none focus:ring-2 focus:ring-sky-500 dark:text-white text-slate-900 transition-all shadow-lg placeholder:text-slate-400 text-sm sm:text-base">
            <button onclick="executeAgent()" class="absolute right-2 top-2 bottom-2 bg-sky-600 hover:bg-sky-500 px-5 rounded-xl text-white transition-all active:scale-95 shadow-lg shadow-sky-900/20">
                <i id="btnStatus" class="fas fa-bolt"></i>
            </button>
        </div>

        <!-- Activity Log (Scrollable) -->
        <div class="pt-4 border-t border-slate-200 dark:border-slate-800">
            <h3 class="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-4 flex items-center gap-2">
                <i class="fas fa-history"></i> Recent Logs
            </h3>
            <div id="activityLogs" class="space-y-2 max-h-32 overflow-y-auto pr-2 custom-scrollbar">
                <p class="text-[11px] text-slate-400 italic">No logs yet.</p>
            </div>
        </div>
    </div>

    <script>
        // --- THEME LOGIC ---
        function toggleTheme() {
            const html = document.documentElement;
            const icon = document.getElementById('themeIcon');
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                html.classList.add('light');
                icon.className = "fas fa-sun";
                localStorage.setItem('theme', 'light');
            } else {
                html.classList.remove('light');
                html.classList.add('dark');
                icon.className = "fas fa-moon";
                localStorage.setItem('theme', 'dark');
            }
        }

        // Initialize Theme
        if (localStorage.getItem('theme') === 'light') {
            document.documentElement.classList.add('light');
            document.getElementById('themeIcon').className = "fas fa-sun";
        } else {
            document.documentElement.classList.add('dark');
        }

        // --- CALCULATION LOGIC ---
        async function executeAgent() {
            const inputField = document.getElementById('agentInput');
            const icon = document.getElementById('btnStatus');
            const query = inputField.value;
            if(!query) return;

            // Haptic Feedback for Mobile
            if(navigator.vibrate) navigator.vibrate(20);

            icon.className = "fas fa-spinner animate-spin";
            
            try {
                const response = await fetch('/api/calculate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({query: query})
                });
                const result = await response.json();
                
                if(result.status === 'success') {
                    document.getElementById('expView').innerText = result.data.expression + " =";
                    document.getElementById('resultView').innerText = result.data.result;
                    logActivity(query, result.data.result);
                    inputField.value = "";
                } else {
                    alert(result.message);
                }
            } catch (error) {
                alert("Agent Offline");
            } finally {
                icon.className = "fas fa-bolt";
            }
        }

        function logActivity(q, r) {
            const container = document.getElementById('activityLogs');
            if(container.innerText.includes("No logs yet")) container.innerHTML = '';
            
            const div = document.createElement('div');
            div.className = "flex justify-between items-center bg-white dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200 dark:border-slate-800/40 text-[11px] mb-2 shadow-sm animate-pulse";
            div.innerHTML = `<span class="dark:text-slate-400 text-slate-600 font-medium">${q}</span><span class="text-sky-500 font-mono font-bold">${r}</span>`;
            
            container.prepend(div);
            setTimeout(() => div.classList.remove('animate-pulse'), 500);
        }

        function copyToClipboard() {
            const val = document.getElementById('resultView').innerText;
            navigator.clipboard.writeText(val);
            const icon = document.getElementById('copyIcon');
            icon.className = "fas fa-check text-green-500";
            setTimeout(() => { icon.className = "far fa-clone text-lg sm:text-xl"; }, 2000);
        }

        async function clearMemory() {
            await fetch('/api/clear', {method: 'POST'});
            location.reload();
        }
    </script>
</body>
</html>
