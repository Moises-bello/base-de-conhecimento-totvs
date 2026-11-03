---
content_hash: eb0d3cd4ad00c351e8750b35808381098a06d8e055425ddc44b93c7b19e92d2d
fetched_at: '2026-06-29T00:10:45.870320+00:00'
page_id: '553339435'
product: rm
source: tdn-rm
title: '9035032 FISCAL01-13327 DT SPED Fiscal: Registro 1400 - Resolução 5.369 MG'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553339435
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 9035032 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13327 |

## **02. SITUAÇÃO/REQUISITO**

Segundo a legislação abaixo o cliente precisa gerar o registro 1400 referente a operações de transporte.

Resolução 5.369 de 22 de maio de 2020. Item 3.4 - Da Prestação de Serviço de Transporte Rodoviário. Veja resolução no link abaixo:  
[http://www.fazenda.mg.gov.br/empresas/legislacao\_tributaria/resolucoes/2020/rr5369\_2020.html](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/resolucoes/2020/rr5369_2020.html "Follow link")

Tratar a geração do Registro 1400 no SPED Fiscal para pegar o Município da Coleta quando o Município do Serviço não estiver preenchido, independente do modelo do documento.

## **03. SOLUÇÃO**

Ajuste na geração do registro 1400 do SPED Fiscal para pegar o Município da Coleta quando o Município do Serviço não estiver preenchido.

       Considerando a regra do registro 1400 do SPED Fiscal foi implementado a seguinte consistência na geração do 1400, sendo um lançamento:

* **Município da Coleta preenchido +  Município do Serviço preenchido** = Gerar 1400 com o código  **Município do Serviço**
* **Município da Coleta NÃO preenchido +  Município do Serviço preenchido** = Gerar 1400 com o código  **Município do Serviço**
* **Município da Coleta preenchido +  Município do Serviço NÃO preenchido =**Gerar 1400 com o código  **Município de Coleta**
* **Município da Coleta NÃO preenchido +  Município do Serviço NÃO preenchido = Não gerar o 1400**
