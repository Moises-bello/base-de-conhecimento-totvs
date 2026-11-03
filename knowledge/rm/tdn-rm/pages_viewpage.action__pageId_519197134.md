---
content_hash: 45aff73b9b50aec5d0337f9733b2aec6a1bdd414e48de58fd752680fee9c2867
fetched_at: '2026-06-29T00:10:30.101245+00:00'
page_id: '519197134'
product: rm
source: tdn-rm
title: FISCAL01-10377 DT EFD-REINF Implementação da geração do Evento R-2060
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519197134
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração dos Eventos da REINF |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10377 |

**02. SITUAÇÃO/REQUISITO**

Implementação Contribuição Previdenciária sobre a Receita Bruta - CPRB, Evento R-2060 da Reinf.

**03. SOLUÇÃO**

Implementação do evento R-2060 da REINF.

* Detalhes da Implementação:

No campo **Código Ato Cotepe** do lançamento Outros Débitos e Créditos, a quantidade máxima de caracteres foi aumentado para 10 caracteres, o código da atividade econômica deve ser preenchimento neste campo.  

No Cadastro do Evento foi Implementado a origem período de apuração que será exibido para o evento R-2060.

Foi implementado a tabela DEVENTOREINFPERCONPREV para que seja salvo a origem dos dados da apuração da contribuição previdenciária do evento R-2060.

Implementação do serviço de geração dos eventos R-2060 , disponibilização na API e Processo de Geração de Eventos.

* Alterações genéricas a todos os eventos:

Será considerado a versão definida nos parâmetros para geração dos eventos 20XX da Reinf.  
Será gravado o histórico de inclusão dos eventos quando realizado a geração dos eventos.
