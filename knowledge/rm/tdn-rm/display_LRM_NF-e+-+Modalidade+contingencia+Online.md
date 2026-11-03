---
content_hash: 04ff60208498abda1d6c668a3ccbc27e265a25e37d09fc2cc119d94c5656c68e
fetched_at: '2026-06-29T00:11:12.307069+00:00'
page_id: '65209290'
product: rm
source: tdn-rm
title: NF-e - Modalidade contingencia Online
type: documentation
url: https://tdn.totvs.com/display/LRM/NF-e+-+Modalidade+contingencia+Online
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.20* |
| **Processo** | **:** | Modalidade contingencia Online |
| **Subprocesso** | **:** | Modalidade contingencia Online |
| **Data da publicação** | **:** | 05/07/2013 |

**Introdução:**

Sendo identificado qualquer fator que impeça a transmissão das NF-e e/ou obtenção da autorização

de uso por um problema na SEFAZ, a empresa pode adotar a Contingência Online (SCAN), caso o sistema esteja em operação para a sua UF. Normalmente a SEFAZ de origem disponibiliza no site um aviso informando a situação SCAN habilitada:

Esta modalidade de operação deverá ser utilizada apenas quando a Sefaz autorizar a emissão de NF-e no modo Contingência Online (SCAN). 

Para isso, devem-se acessar o menu Utilitários | Sped | NF-e Estadual | Processos | Alterar Modalidade de Operação:

**Observações:**

Ao alterar a modalidade para “Contingência Online”, devem-se observar os seguintes procedimentos:

1 – Monitorar o status do serviço do SCAN para verificar se o serviço está disponível para sua UF;

2 – Geração de novo arquivo XML da NF-e com o campo “tp\_emis” alterado para 3. Isto o RM faz automaticamente.

**Caso o movimento tenha sido enviado anteriormente para a modalidade “NORMAL” e esteja com o status “PENDENTE” é necessário realizar a emissão de um novo movimento para o envio da NF-E na modalidade Contingência Online.**

**Isto porque o lote que realizou a transmissão desta nota pode ter sido recebido pela SEFAZ, mas o Web Service da SEFAZ não retornou os dados da autorização da nota.**

**Quando o serviço for estabelecido, a nota que se encontrava com o status Pendente no sistema, deverá ser consultada, buscando assim os dados de autorização da mesma para posteriormente ser cancelada, uma vez que a nota que terá valor fiscal será a nota enviada e aprovada em contingência Online (SCAN).**

3 – Alterar a série do novo movimento para a faixa de uso exclusivo do SCAN (900 a 999). A alteração da série implica na alteração da numeração da NF-e, uma vez que alterando a série, automaticamente a numeração é alterada.

4 – Transmissão da NF-e para o SCAN e obtenção da autorização de uso;(Ao contrário da Contingência Offline, o SCAN é enviado à SEFAZ normalmente e consultado a sua autorização)

5 – Impressão do DANFE em papel comum;

6 – Após o Web Service da SEFAZ estar disponível novamente, o emissor deve voltar à modalidade de operação para “NORMAL” e voltar à série de origem. Automaticamente o sistema irá continuar a sequencia de numerações da NF-e que foi interrompida anteriormente.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
