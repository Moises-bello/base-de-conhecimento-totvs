---
article_id: 360046402253
category: RH - MANAD
content_hash: 99825d72fd058e0673570ca1661df97b64a7042dc6101ac1ca729a641eec985a
fetched_at: '2026-06-28T22:43:33.832393+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na validação MANAD: Arquivo não está no padrão
  MANAD ou a primeira linha de identificação é inválida'
type: support-article
updated_at: '2021-04-06T20:21:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046402253-RH-Linha-Protheus-GPE-Erro-na-valida%C3%A7%C3%A3o-MANAD-Arquivo-n%C3%A3o-est%C3%A1-no-padr%C3%A3o-MANAD-ou-a-primeira-linha-de-identifica%C3%A7%C3%A3o-%C3%A9-inv%C3%A1lida
---

**Ocorrência:**Erro na validação MANAD: Arquivo não está no padrão MANAD ou a primeira linha de identificação é inválida  
**Ambiente:**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17

**Causa:**Esse incidente ocorre, pois a parametrização do processamento do MANAD (Wizard), está incompleta.   
  
**Solução**

1) Erro apresentado no validador para arquivo MANAD:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065611833/mceclip0.png)  
  
2) Arquivo MANAD apresentando primeira linha inválida:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065612133/mceclip1.png)

3) Para geração do Registro tipo 0000 – Abertura do arquivo digital e identificação dos estabelecimentos do contribuinte as informações referentes a este registro serão baseadas no Cadastro da Empresa, bem como nos parâmetros informados no assistente da rotina.  
  
**Acesse o Módulo 09 - Livros Fiscais:** Miscelânea-> Arquivos Magnéticos -> Instruções Normativas e na tela Passo 1/7 do WIZARD informe as filiais selecionadas:   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064623474/mceclip2.png)  
  
4) Apresentação do arquivo com a primeira linha válida:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065614573/mceclip3.png)  
  
**Saiba Mais**[Artigos sobre Manad](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360008157193-RH-MANAD)
