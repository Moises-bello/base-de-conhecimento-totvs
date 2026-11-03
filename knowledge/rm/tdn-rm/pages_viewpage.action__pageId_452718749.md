---
content_hash: 88a41e739276f795c2b99eab8a8b20124cdb49409d7cb9f0526c4d8edfb73d43
fetched_at: '2026-06-29T00:10:01.474971+00:00'
page_id: '452718749'
product: rm
source: tdn-rm
title: Processo de Suspensão de Incidência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718749
version: 7
---

Caso a empresa possua processos administrativos ou judiciais com decisão/sentença favorável, determinando a não incidência de contribuição previdenciária, sindical, FGTS ou imposto de renda sobre a rubrica identificada no evento, essas informações deverão ser incluídas neste registro. O detalhamento do processo deverá ser realizado através de um evento específico na tabela de processos.  
   
**Tributo**  
Determinar para qual tributo será o processo criado.  
   
**N° do Processo**  
Preencher com o número do processo referente  a não incidência.  
Observações:

* Caso possua integração com o RM Vitae (Gestão de Pessoal), será possível fazer a busca dos processos judicias existentes no mesmo através da "Lupa".
* Se o tributo não for informado ou seja do tipo INSS, o sistema retornará os processos do tipo "Administrativo e Judicial".
* Caso o tributo seja diferente do tipo "INSS", o sistema retornará os processos do tipo "Judicial".
* As informações apresentadas neste registro, serão enviados ao eSocial nos eventos S-2399  e S-1010.
* Maiores detalhes sobre a formatação do Número do Processo Jurídico: Processos Jurídicos.

**Código do Indicativo da Suspensão**  
Preencher com o código da suspensão da incidência em questão conforme processo jurídico.

   
**Extensão da Decisão/Sentença**  
Determinar qual é a decisão/sentença da suspensão da incidência.  
Observação: O campo ficará disponível apenas se o tributo for do tipo INSS.

   
**Tipo do Processo**  
Deverá ser Judicial ou Administrativo quando o tributo for INSS, para os demais tributos, será como default Judicial

**Depósito do Montante Integral**

Ao marcar esse parâmetro na geração do Relatório de Conferência INSS Patronal, os valores da base da folha passam a ser considerados para a comparação com os valores retornados pela DCTFWeb.

**Indicativo de Suspensão da Exigibilidade**

Ao preencher este campo, na geração do Relatório de Conferência INSS, os valores da base da folha passam a ser considerados para a comparação com os valores retornados pelo RET.
