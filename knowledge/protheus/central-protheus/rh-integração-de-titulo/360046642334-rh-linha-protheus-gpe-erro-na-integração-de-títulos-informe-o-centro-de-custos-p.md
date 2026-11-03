---
article_id: 360046642334
category: RH - Integração de Titulo
content_hash: ad3cf3a6be847ca997e2e58bdf6ae6c3e9477f954c6e4bac8913ab291f67376e
fetched_at: '2026-06-28T22:43:36.320921+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos: Informe o Centro
  de Custos para prosseguir'
type: support-article
updated_at: '2025-08-08T17:05:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046642334-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-Informe-o-Centro-de-Custos-para-prosseguir
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33463033169303)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Na integração de títulos é apresentada a mensagem: Erro na inclusão de título a pagar - Informe o centro de custos para prosseguir.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**Esse incidente ocorre, pois no Módulo financeiro, o campo de centro de custos (E2\_CCUSTO), está configurado como obrigatório, ou o parâmetro **[MV\_PCOINTE](https://tdn.totvs.com/pages/releaseview.action?pageId=837449847)** está habilitado.   
  
**Solução  
Erro apresentado:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067000454)**  
Para solucionar essa ocorrência, temos estas opções:   
  
1- Desabilitar o campo **E2\_CCUSTO** no Módulo financeiro, através do Configurador.  
obs: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas referente aos pagamentos do Centro de Custo.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_CCUSTO / Aba Uso e desmarcar o campo Obrigatório:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068083533)

2. Verificar via CONFIGURADOR se os campos E2\_CCC / E2\_CCD,  possuem alguma validação de usuário que impede o campo ser gravado vazio ou validação específica:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18025809038487)

3. Verifique se o parâmetro **[MV\_PCOINTE](https://tdn.totvs.com/pages/releaseview.action?pageId=837449847),** está habilitado;

4. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.   
  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada GP670ARR que permite a gravação de outros campos.   
Por exemplo, caso seja necessário que os campos E2\_CCC e E2\_CCD sejam gravados com o conteúdo do campo RC1\_CC, poderá utilizar o ponto de entrada, conforme o *link* disponibilizado abaixo:  
[RH - Linha Protheus - GPE - Funcionalidade do ponto de entrada GP670ARR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17185007211671-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-entrada-GP670ARR)  
 **IMPORTANTE:**Mesmo o título na manutenção de títulos possuindo centro de custo informado , o processo de integração não gravará o campo centro de custo sem o ponto de entrada mencionado.   
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Integração de titulo entre Gestão de Pessoal e Financeiro, não preenche campo centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012562571-MP-GPE-Integra%C3%A7%C3%A3o-de-titulo-entre-Gest%C3%A3o-de-Pessoal-e-Financeiro-n%C3%A3o-preenche-campo-centro-de-custo?source=search)  
[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
