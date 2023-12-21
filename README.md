# Network Discover

Bu Python programı, ağ tarama işlemlerini gerçekleştirmek için scapy kütüphanesini kullanır.

## Kullanım

1. Python yüklü değilse [Python'un resmi web sitesinden](https://www.python.org/downloads/) indirip yükleyin.
2. Gerekli kütüphaneyi yüklemek için terminal veya komut istemcisine şu komutu yazın:

    ```bash
    pip install scapy
    ```

3. `network_discover.py` dosyasını düzenleyerek hedef IP aralığını güncelleyin:

    ```python
    target_ip = "10.0.2.0/24"  # Hedef IP aralığınızı güncelleyin
    ```

4. Programı çalıştırmak için terminal veya komut istemcisine şu komutu yazın:

    ```bash
    python network_discover.py
    ```

---

**Not:** Ağ taraması etik kullanım ve izinli sistemler üzerinde gerçekleştirilmelidir. Yasal ve etik kurallara uymak önemlidir.
