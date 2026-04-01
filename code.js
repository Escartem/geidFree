const mod = Process.getModuleByName("downloader.exe");
const base = mod.base;
  
Interceptor.attach(base.add(0x17EC2C), {
	onEnter(args) {
		const a1 = this.context.eax;
		const a2 = this.context.edx;

		const s1 = a1.readPointer().readCString();
		const s2 = a2.readPointer().readCString();

		console.log("cmp:", s1, s2);

	  // console.log(`[-] cmp ${args[0].readU32()} -> ${args[1].readU32()}`)
	}
});

// md5
Interceptor.attach(base.add(0x13E88), {
    onEnter(args) {
        const src = args[1];   // void *Src
        const len = args[2];   // int a3
        console.log(len);

        this.input = src.readByteArray(parseInt(len));
        console.log("MD5 input:", src.readUtf8String());
    },
    onLeave(retval) {
        const out = this.context.eax; // return buffer (a4)
        console.log("MD5 done");
    }
});

Interceptor.attach(base.add(0x13454), {
    onEnter(args) {
        this.out = args[1]; // a4 (digest buffer)
    },
    onLeave() {
        const bytes = this.out.readByteArray(16);
        console.log("MD5:", hexdump(bytes));
    }
});