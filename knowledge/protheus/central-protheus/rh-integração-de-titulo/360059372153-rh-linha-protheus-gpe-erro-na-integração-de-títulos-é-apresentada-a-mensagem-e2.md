---
article_id: 360059372153
category: RH - Integração de Titulo
content_hash: b421b0717d1d0237d29d02c210e0c53ab60e28ab7294cd4ad4d300c2785be724
fetched_at: '2026-06-28T22:43:37.181651+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos é apresentada a
  mensagem: E2_NATUREZ <-- Inválido'
type: support-article
updated_at: '2025-07-25T20:01:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059372153-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-E2-NATUREZ-Inv%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33723933050647)** Tempo aproximado para leitura: 00:01:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: E2\_NATUREZ <-- Inválido  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro - SIGAFIN**, o campo **Cod. Orcam.** (E2\_CODORCA), está configurado como obrigatório.

**Solução**Erro apresentado:  **![controle_or_amentario.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097514854)**

Para solucionar essa ocorrência, temos duas opções: 

1- Desabilitar o campo **E2\_CODORCA** da SE2 no Módulo Financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_CODORCA/ Aba Uso e desmarcar o campo Obrigatório:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33723927103895)

2- Caso a empresa faça uso do controle orçamentário através do Modulo **Planejamento e Controle Orçamentário - SIGAPCO**, na rotina **Natureza - FINA010** deve ser informado uma conta contábil, essa informação deve ser inserida no campo **Cta. Contábil** (**ED\_CONTA**).

![controle_or_amentario_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097522494)

Após este processo o título que foi invalidado deve ser gerado novamente e posteriormente integrado.  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
