% Fungsi keanggotaan untuk Permintaan
function mu = permintaan(x)
    if x < 2000
        mu = (2000 - x) / 2000;
    elseif x >= 2000 && x <= 3000
        mu = 1;
    elseif x > 3000 && x < 4000
        mu = (4000 - x) / 1000;
    else
        mu = 0;
    end
end

% Fungsi keanggotaan untuk Persediaan
function mu = persediaan(y)
    if y < 200
        mu = (200 - y) / 200;
    elseif y >= 200 && y <= 400
        mu = 1;
    elseif y > 400 && y < 600
        mu = (600 - y) / 200;
    else
        mu = 0;
    end
end

% Fungsi untuk menghitung produksi berdasarkan fuzzy rules
function rules = fuzzy_inference(per, pers)
    rules = [];
    if strcmp(per, 'turun')
        if strcmp(pers, 'sedikit')
            rules = [rules, 1];  % Produksi Bertambah
        elseif strcmp(pers, 'sedang') || strcmp(pers, 'banyak')
            rules = [rules, 0];  % Produksi Berkurang
        end
    elseif strcmp(per, 'tetap')
        if strcmp(pers, 'sedikit')
            rules = [rules, 1];  % Produksi Bertambah
        else
            rules = [rules, 0];  % Produksi Berkurang
        end
    elseif strcmp(per, 'naik')
        if strcmp(pers, 'sedikit') || strcmp(pers, 'sedang')
            rules = [rules, 1];  % Produksi Bertambah
        else
            rules = [rules, 0];  % Produksi Berkurang
        end
    end
end

% Contoh Input
permintaan_input = 'turun';
persediaan_input = 'sedikit';

% Menghitung keanggotaan
keanggotaan_permintaan = permintaan(1500);  % contoh permintaan
keanggotaan_persediaan = persediaan(100);    % contoh persediaan

% Menghitung produksi
produksi = fuzzy_inference(permintaan_input, persediaan_input);

% Output
disp(['Keanggotaan Permintaan: ', num2str(keanggotaan_permintaan)]);
disp(['Keanggotaan Persediaan: ', num2str(keanggotaan_persediaan)]);
disp(['Produksi berdasarkan aturan: ', num2str(produksi)]);

% Visualisasi
x = linspace(0, 6000, 100);
y_permintaan = arrayfun(@(i) permintaan(i), x);
y_persediaan = arrayfun(@(i) persediaan(i), x);

figure;
subplot(2, 1, 1);
plot(x, y_permintaan, 'Color', 'orange');
title('Fungsi Keanggotaan Permintaan');
xlabel('Jumlah Permintaan');
ylabel('Keanggotaan');
grid on;

subplot(2, 1, 2);
plot(x, y_persediaan, 'Color', 'purple');
title('Fungsi Keanggotaan Persediaan');
xlabel('Jumlah Persediaan');
ylabel('Keanggotaan');
grid on;

sgtitle('Visualisasi Keanggotaan');
