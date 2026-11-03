---
content_hash: 4a129e48d98a340e740dc07b2f471e264bfa5be920ae8cc1fdaaf626ac9ad9de
fetched_at: '2026-07-02T19:24:28.846490+00:00'
page_id: '862610334'
product: protheus
source: tdn-tec
title: DBAccess - Seção [General], chave UseProcDump
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862610334
version: 8
---

Esta chave permite habilitar em **ambiente Windows** o uso de um programa externo (***ProcDump***) para auxiliar na captura e geração de arquivos de *dump* do true.

---

A utilização dessa chave de configuração é recomendada para cenários em **ambiente Windows** quando há a ocorrência de **queda** da aplicação, mas **não** é observada a geração do arquivo de **dump** na pasta de instalação dotrue.

---

* Esta configuração está disponível no true com build igual ou superior a 22.1.1.1
* Recomenda-se que esta configuração seja habilitada apenas se realmente necessário
* Para habilitar este recurso, é necessário utilizar o build **debug** do true
* O ProcDump da SysInternals (adquirida pela Microsoft) pode ser baixado em: <https://learn.microsoft.com/en-us/sysinternals/downloads/procdump>
* O arquivo de dump será gerado na mesma pasta onde está o ProcDump e o true

---

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 | Desabilita a utilização do ProcDump (padrão). |
| 1 | Habilita utilização do ProcDump. |

---

## Exemplo

---

## Procedimentos para utilização

* Baixe o ***ProcDump*** através do site citado nessa documentação
* Após efetuar o download, extraia o conteúdo do pacote na pasta onde está o executável do true
* Proceda com a configuração da chave em questão no dbaccess.ini do ambiente em uso
* Inicie o true **em modo console** e utilize-o até a reprodução do erro e geração do arquivo de *dump*

---

## Veja também
