---
content_hash: 7b7fc69e6064ce98e508f850f9255f1a8cd62ae60fdfaea76396488ba2f3ffab
fetched_at: '2026-06-29T00:11:50.855634+00:00'
page_id: '84541630'
product: rm
source: tdn-rm
title: RMFIS00027_Validação Registro 1900 - CFOP obrigatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541630
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.5x |
| **Processo** | **:** | Validação EFD Contribuições |
| **Subprocesso** | **:** | Registro 1900 - CFOP obrigatório |
| **Data da publicação** | **:** | 17/09/2013 |

 

**Introdução**

Seguem esclarecimentos com relação à validação do arquivo ".txt" do EFD Contribuições na geração do Lucro Presumido (registro 1900).

**Entendimento/Solução da mensagem:**

Este erro ocorre, pois o lançamento que está sendo gerado no arquivo ".txt" possui um Código Modelo de Documento cadastrado no Tipo de Documento vinculado ao processo do F500 do TOTVS Gestão Fiscal.

O processo permite vincular Tipos de Documentos com ou sem modelos de documentos, mas deve ser seguido a seguinte parametrização:

* **Se for vinculado Tipo de Documento com Código Modelo Documento:**Este lançamento deve ter sido gerado (Origem) do RM Nucleus  ou do RM Liber, pois se existe modelo de Documento o mesmo é Fiscal, e sua origem deve estar no RM LIBER. Ao gerar o EFD Contribuições,  o sistema verifica se o lançamento Financeiro também está no RM Liber e, se existir modelo de Documento, busca do Lançamento Fiscal o CFOP desta nota.

**Exemplo:**CFOP 5101 com modelo 01:

 |1900|11111111000191|01|1||00|2000,00|1|02|02|5101|||

* **Se for vinculado Tipo de Documento sem Código Modelo Documento:** O lançamento não tem a necessidade de ter sido gerado/originado no RM Liber, pois se não existe modelo de Documento, quer dizer que este lançamento não é fiscal (ex: recibos de aluguel etc). Na geração do arquivo ".txt" do EFD Contribuições o sistema não vai verificar se o lançamento possui nota no RM Liber e não vai gerar o CFOP no registro 1900:

Exemplo: |1900|11111111000191||||00|999,00|1|02|02||||

**Observações:**

O campo CFOP não é obrigatório, conforme Guia prático do EFD Contribuições, mas se for informado um modelo de Documento  *01,1b,04,06,55* ou *59*, o mesmo se torna obrigatório.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/Fis.Bloco1.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
