---
content_hash: 7f31947f59f49b4c77d181bac1cbb61b1a1c9a8c591200f68bdafcff115fc13d
fetched_at: '2026-07-02T19:24:25.775868+00:00'
page_id: '506381921'
product: protheus
source: tdn-tec
title: IniCustomization
type: documentation
url: https://tdn.totvs.com/display/tec/IniCustomization
version: 3
---

BLOCK

IniCustomization

## IniCustomization

Permite a utilização de um arquivo de configuração adicional ao atual, considerando que todas as chaves do ini customizado terá prioridade ao atual, quando o TOTVS | Application Server for ler ou escrever uma chave de ini.

### Valores válidos

| Valor | Descrição |
| --- | --- |
| <<caminho>> | Indique o caminho completo de onde se encontra o arquivo de ini customizado |

### Comportamentos de leitura e escrita

Quando se está com essa chave de ini ativada, ao se utilizar comandos que leem, deletam ou escrevem no arquivo de ini, ele seguirá os seguintes comportamentos:

* **Leitura**: supondo que no ini customizado exista a chave "consolelog=0" na seção [General], ao contrario da chave "consolelog=1" na seção [General] do ini padrão, o consolelog está desligado, já que **a leitura do ini customizado tem prioridade**.
* **Escrita**: caso seja utilizado qualquer função que escreve no ini, quando o ini customizado está ativo, **toda a escrita será realizado no ini customizado**.
* **Deleção**: caso seja utilizado qualquer função que deleta configurações no ini, quando o ini customizado está ativo, **a deleção ocorrerá no ini customizado e ini padrão**.

### **Exemplo**

```
[General]  
IniCustomization=/totvs/data/inicustom.ini
```

| Importante |
| --- |
| Essa chave de ini pode ser utilizada apenas em versões iguais ou superiores a versão 17.3.0.14  do  TOTVS | Application Server e atualmente só está disponível para Linux. |
