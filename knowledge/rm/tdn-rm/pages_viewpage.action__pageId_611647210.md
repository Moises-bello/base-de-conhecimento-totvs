---
content_hash: 0ccbda4ad6ea8fbdf9584b10af3342a1d651016f3990eb5b44467fb269aaa316
fetched_at: '2026-06-29T00:10:59.169791+00:00'
page_id: '611647210'
product: rm
source: tdn-rm
title: Relatórios ADRC-ST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611647210
version: 45
---

Para a rotina ADRC-ST, temos as Consultas SQL

* **FISSQLANEX0021 - ADRC-ST - Registro 1110.TotvsConsSQLAnex**
* **FISSQLANEX0022 - ADRC-ST - Registro 1120.TotvsConsSQLAnex**
* **FISSQLANEX0002 - ADRC-ST - Registro 1210.TotvsConsSQLAnex**
* **FISSQLANEX0003 - ADRC-ST - Registro 1220.TotvsConsSQLAnex**
* **FISSQLANEX0019 - ADRC-ST - Registro 1310.TotvsConsSQLAnex**
* **FISSQLANEX0020 - ADRC-ST - Registro 1320.TotvsConsSQLAnex**
* **FISSQLANEX0019 - ADRC-ST - Registro 1410.TotvsConsSQLAnex**
* **FISSQLANEX0020 - ADRC-ST - Registro 1420.TotvsConsSQLAnex**
* **FISSQLANEX0017 - ADRC-ST - Registro 1510.TotvsConsSQLAnex**
* **FISSQLANEX0018 - ADRC-ST - Registro 1520.TotvsConsSQLAnex**

As consultas acima exibem os Lançamentos Fiscais de determinado período que serão considerados na ADRC-ST nos registros [1110](https://tdn.totvs.com/display/public/LRM/Registro+1110), [1120](https://tdn.totvs.com/display/public/LRM/Registro+1120), [1210](https://tdn.totvs.com/pages/viewpage.action?pageId=553906003), [1220](https://tdn.totvs.com/pages/viewpage.action?pageId=553906006) , [1310](https://tdn.totvs.com/pages/viewpage.action?pageId=553906013), [1320](https://tdn.totvs.com/pages/viewpage.action?pageId=553906017), [1410](https://tdn.totvs.com/display/LRM/Registro+1410) , [1420](https://tdn.totvs.com/display/LRM/Registro+1420), e .

IMPORTANTE!

* Os arquivos das Consultas SQL estão disponíveis em [Totvs Compartilhamento](https://tdn.totvs.com/x/WJrCF)
* Devido a limitação da consulta, os seguintes campos não serão demonstrados, conforme gerado na rotina do ADRC-ST:

  + 13, 14 e 15 dos registros **[1210](https://tdn.totvs.com/pages/viewpage.action?pageId=553906003)** e **[1220](https://tdn.totvs.com/pages/viewpage.action?pageId=553906006)**
  + 13, 14, 15 e 16 dos registros **[1110](https://tdn.totvs.com/display/public/LRM/Registro+1110)** e **[1120](https://tdn.totvs.com/display/public/LRM/Registro+1120)**
  + 13, 14 e 15 dos registros **[1310](https://tdn.totvs.com/pages/viewpage.action?pageId=553906013)**e **[1320](https://tdn.totvs.com/pages/viewpage.action?pageId=553906017)**
  + 13, 14 e 15 dos registros **[1410](https://tdn.totvs.com/display/LRM/Registro+1410)**e **[1420](https://tdn.totvs.com/display/LRM/Registro+1420)**
  + 13, 14 e 15 dos registros **1510** e .

**Importando Consultas SQL**

Acesse **Período de Apuração | Anexos | Consultas SQL**

Clique em **Adicionar Objetos**e selecione o arquivo da Consulta SQL a ser importado 

Parametrize as consultas conforme demonstrado nas imagens abaixo:

IMPORTANTE!

* Para o correto funcionamento do relatório, as Consultas SQL devem ser anexadas ao **Período de Apuração**

## **Executando o relatório**

Após a importação das Consultas SQL, as mesmas estarão disponíveis no menu **Período de Apuração | Anexos | Consultas SQL**

Ao selecionar um **Período de Apuração** do tributo **ICMSST,** do lado direito serão listados os registrosreferentes ao período.

O usuário poderá exportar os dados em diversos formatos, conforme sua necessidade
