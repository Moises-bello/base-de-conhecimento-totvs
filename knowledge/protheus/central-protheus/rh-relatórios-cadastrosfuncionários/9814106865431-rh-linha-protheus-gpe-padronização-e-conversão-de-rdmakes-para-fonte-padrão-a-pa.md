---
article_id: 9814106865431
category: RH - Relatórios Cadastros/Funcionários
content_hash: 419d62daa1e64b999d55982983081f3fd93e85b50b15e22f3ca739d80284edb4
fetched_at: '2026-06-28T22:43:18.457843+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: RH - Linha Protheus - GPE - Padronização e conversão de Rdmakes para fonte
  padrão a partir da versão 12.1.33
type: support-article
updated_at: '2025-07-25T11:07:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9814106865431-RH-Linha-Protheus-GPE-Padroniza%C3%A7%C3%A3o-e-convers%C3%A3o-de-Rdmakes-para-fonte-padr%C3%A3o-a-partir-da-vers%C3%A3o-12-1-33
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31640552779159) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Padronização e conversão de Rdmakes para fonte padrão a partir da versão 12.1.33  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.33  
  
**Solução**Alguns relatórios do Sistema estava sendo utilizado **funções de usuário,** o qual obrigava o usuário compilar o Rdmake no ambiente.  
Com a compatibilização no release 12.1.33  é necessário alterar a **chamada** dessas funções no **Menu,** caso queiram utilizá-los como **rotina /** fonte padrão, **substituindo** por **função padrão do Protheus** através do **Configurador.**

Como exemplo, atualizamos a rotina de **Integração com Word:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9813800754839)**

No campo **Programa,** informamos o conteúdo **GPER987** (conforme tabela abaixo) e o **tipo** como **Função Protheus**

**SIGAGPE**

| Item | Function | Chamada Menu |
| --- | --- | --- |
| Integração Benefícios | BENEFARQ | GPEM931 |
| Recibo Pag. Elet. Itaú | RECITAU | GPEM933 |
| Recibo Pag. Elet. Santand | RECSANT | GPEM934 |
| Seguro Desemprego | SEGDES | GPEM935 |
| Anonimização dados | GPEM932 | GPEM936 |
| Recibo Pag. Elet. Bradesco | RECBRAD | GPEM937 |
| Consignado Folha Pagto | GPCONSIG | GPEM938 |
| Etiq. Aumento Salarial | ETIQAS | GPER981 |
| Etiq. Contrato Trabalho | ETIQCT | GPER982 |
| Etiq. Anotações Férias | ETIQFER | GPER983 |
| Etiq. Mala Direta | ETIQMD | GPER984 |
| Etiq. Data Opção FGTS | ETIQOPC | GPER985 |
| PPP – Perfil Profiss. Prev. | GPERPPP | GPER986 |
| Admissão | GPEWORD | GPER987 |
| CAT – Com. Acid. Trab. | IMPCAT | GPER988 |
| Dirf Mensal Darf PIS Dirf / Darf | IMPDARF | GPER989 |
| Recibo Férias | IMPFER | GPER990 |
| Impressão GPS | IMPGPS | GPER240 |
| Guia INSS | IMPGRPS | GPER992 |
| Contribuições Sindicais | IMPGRCS | GPER993 |
| Rescisão | IMPGRFC | GPER994 |
| DIRF Form. Cont. | IMPIRPF | GPER995 |
| Comp. Rend. P.J. | IMPIRPJ | GPER996 |
| Rescisão | IMPLIFIN | GPER997 |
| Modelo Documentos | IMPMODEL | GPER998 |
| Rescisão | IMPRESC | GPER999 |
| Rescisão | IMPRESG | GPER1000 |
| Rescisão | IMPRESH | GPER1001 |
| Rescisão | IMPRESZ | GPER1002 |
| RPA – Rec. Pag. Auton. | IMPRPA | GPER1003 |
| Reajuste Tarefas | REAJTAR | GPER1004 |
| Captura Foto | CAPFOTO | GPER1018 |
| Arq. Lei Transparência | GPER023 | GPER1019 |
| Etiqueta Cartão Ponto | IMPETIQ | GPER1020 |
| Guia Recol. Resc. FGTS | IMPGREC | GPER1021 |
| Rel. Aum. Salarial | RAUMSAL | GPER1022 |
| Termo Realiz. Estágio | REAEST | GPER1023 |

**Importante**É necessário rodar **UPDDISTR** para aplicação de pacote de atualização disponível a partir da expedição de 16/11/21 referente Perguntas (SX1) para adequação do grupo de perguntas descrito abaixo:

| X1\_GRUPO | X1\_ORDEM | X1\_VALID |
| --- | --- | --- |
| IMPMODEL | 09 | fOpcModelo() |

Caso não queira utilizar esta nova funcionalidade, será necessário compilar o RdMake padrão.

**Saiba Mais**[DT Implementação da padronização de rdmakes](https://tdn.totvs.com/pages/viewpage.action?pageId=644718698)  
[RH - Linha Protheus - GPE - Como excluir ou incluir rotinas no menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013342191-RH-Linha-Protheus-GPE-Como-excluir-ou-incluir-rotinas-no-menu?source=search)  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) os RDMAKES de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044814174-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-os-RDMAKES-de-RH?source=search)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como compilar fontes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019132991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-compilar-fontes?source=search)
