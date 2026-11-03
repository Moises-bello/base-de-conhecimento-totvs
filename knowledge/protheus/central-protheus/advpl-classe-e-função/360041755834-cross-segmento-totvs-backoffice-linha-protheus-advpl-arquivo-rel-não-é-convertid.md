---
article_id: 360041755834
category: ADVPL - Classe e Função
content_hash: 41400aba07605e3b2887bf42b705959a6bfd9191233c5c57600a8fd845853996
fetched_at: '2026-06-28T22:40:14.383964+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Arquivo .REL não
  é convertido em PDF
type: support-article
updated_at: '2023-11-09T11:32:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041755834-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Arquivo-REL-n%C3%A3o-%C3%A9-convertido-em-PDF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao utilizar a classe **FWMsPrinter** a rotina só gera o arquivo **.rel** mas não é transformado em **.pdf**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.17  
  
**Solução**Esse cenário ocorre quando o sistema não encontra os executáveis necessário para a correta execução e geração do arquivo.

Para a correta geração do arquivo, é necessário que estejam disponibilizados nas pastas **SmartClient** e **AppServer** o executável  **TOTVS Printer**

* A versão mais atualizada do binário **TOTVS Printer** é disponibilizado para download em um pacote individual no portal do cliente no mesmo local onde é encontrado os pacotes **TOTVS | Application Server** e **TOTVS | SmartClient**
* A instalação do agente TOTVS Printer é bem simples, basta descompactar o pacote e copiar o mesmo arquivo binário para a pasta de instalação do **TOTVS | Application Server** e **TOTVS | SmartClient.**

A **TOTVS Printer** está disponível nos seguintes pacotes:

| Destino | Pacote |
| --- | --- |
| Application Server 32-bit ou SmartClient 32-bit para Windows | printer\_win32.zip |
| Application Server 64-bit ou SmartClient 64-bit para Windows | printer\_win64.zip |
| Application Server 32-bit ou SmartClient 32-bit para Linux | printer\_linux32.tar.gz |
| Application Server 64-bit ou SmartClient 64-bit para Linux | printer\_linux64.tar.gz |
| SmartClient para Mac**¹** | printer\_mac.zip |
| Application Server 32-bit em Linux sem interface gráfica**²** | pdfprinter\_linux32.tar.gz |
| Application Server 64-bit em Linux sem interface gráfica**²** | pdfprinter\_linux64.tar.gz |

**¹** Exclusivamente para o **Sistema Operacional Mac**, o **TOTVS | SmartClient** já é disponibilizado no portal de downloads com o binário **TOTVS** **Printer** atualizado e embutido no arquivo de instalação (.dmg). Posteriormente é possível atualizar o agente **TOTVS** Printer. (veja em saiba mais)

**²**Agente **TOTVS Printer** especial para ser usado somente quando o **TOTVS Application Server** estiver rodando em um sistema operacional Linux sem interface gráfica (GUI). (veja em saiba mais)

**Importante**:  
Verificar se esses executáveis estão atualizados com a ultima versão disponível no Portal do cliente.  
  
**Saiba mais**[TOTVS Printer - Instalação](https://tdn.totvs.com/pages/viewpage.action?pageId=364910001)  
[Agente TOTVS Printer para Linux sem GUI](https://tdn.totvs.com/display/tec/Agente+TOTVS+Printer+para+Linux+sem+GUI)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como atualizar o Totvs Printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020375912)  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Como verificar a versão da TOTVS printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020375572)
