---
article_id: 5278457304855
category: Faturamento - Cadastros
content_hash: 0fc8fcae59af9a9e80e0f7e17d7ad91f36dccb91a3aa1f34015ac6abb3e23a40
fetched_at: '2026-06-28T22:38:35.560497+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Principais
  duvidas sobre a descontinuidade do MATA030
type: support-article
updated_at: '2024-04-04T13:26:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5278457304855-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Principais-duvidas-sobre-a-descontinuidade-do-MATA030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15370058298775) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Principais dúvidas sobre a descontinuidade do MATA030 e procedimentos a serem executados  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

Sobre a descontinuidade do MATA030, que ocorreu a partir de 04/04/2022, surgiram muitas dúvidas de como passaria a atuação da rotina relacionada ao cadastro de clientes, segue as principais dúvidas e os procedimentos a serem executados:

**1 - Preciso aplicar algum pacote específico para que haja a mudança da rotina MATA030 para a nova rotina de clientes CRMA980?**

Não precisa, não há um pacote específico para esta mudança, o que é preciso fazer é apenas ativar o parâmetro MV\_MVCSA1 para .T. e o sistema já fará o reconhecimento da nova rotina.

**2 - Preciso mudar o menu para a chamada da MATA030 atuar com o CRMA980?**

Não é preciso fazer alteração de menu, que é preciso fazer é apenas ativar o parâmetro MV\_MVCSA1 para .T. e o sistema já fará o reconhecimento da nova rotina.

A alteração do menu será efetuada a partir da nova release 12.1.2210, quando esta release estiver vigente, o parâmetro será descontinuado.

**3 - Ativei o parâmetro MV\_MVCSA1 e ainda aparece a rotina como MATA030, o que fazer?**

O sistema ainda demonstrará como primeiro fonte o MATA030, mas se olhar a stack da rotina, verá que existe a chamada do CRMA980 em paralelo ao MATA030, indicando que a mudança do parâmetro para .T. funcionou.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5268277290775)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5268299856791)

**4 - Haverá alguma trava do sistema para que não seja utilizado o MATA030?**

Não haverá nenhuma trava do sistema, os clientes que não se sentirem seguros no momento para a mudança e quiserem testar, ainda poderão utilizar o MATA030, porém, é uma rotina obsoleta, em caso de erro, a mesma não pois mais manutenção ou evolução por melhoria.

**5 - A MATA030 continuará recebendo algum tipo de melhoria?**

Não, a partir de 04/04/2022, a rotina passa a ficar obsoleta, em caso de erro, a mesma não pois mais manutenção ou evolução por melhoria, toda manutenção e melhoria serão efetuadas no CRMA980.

**6 - Com a descontinuidade da rotina MATA030, como serão tratadas as integrações por EAI para o cadastro de cliente?**

As integrações por EAI ao cadastro de cliente não sofrerão mudanças, inclusive para os pontos de entrada que a integração utiliza, pois, hoje, a rotina **CRMA980** que substituirá a **MATA030**, já possui em sua codificação alguns desvios que identificam que se for **XML**, usar o **MATI030**, se for **Json**, usar o  **MATI030O**.

Caso o parâmetro **MV\_MVCSA****1** estiver habilitado para usar o **CRMA980** , o adapter precisará estar cadastrado para a rotina CRMA980 e não MATA030.

Isso também serve para os pontos de entrada do EAI contidos nas rotinas de integração, que não sofrerão alteração.

**7 - Os pontos de entrada do MATA030 deverão ser  mudados com o uso do CRMA980?**

Sim, para os pontos de entrada existe um de/para do ponto de entrada do MATA030 e qual é o equivalente em mvc no CRMA980. Para acessar a tabela de/para de pontos de entrada, acesse: <https://tdn.totvs.com/x/OtMDJ>

**8 - É necessária adaptação na chamada do ExecAuto do MATA030(Cadastro de Clientes) com o uso do CRMA980?**

Não será necessário a alteração da chamada via ExecAuto/MSExecAuto.

**9 - A partir de qual release será efetuado a mudança de substituição do MATA030 para o CRMA980?**

A partir da última release vigente, 12.1.27 em diante.

**10 - Como ajustar a  ordem de agrupamento de campos customizados após descontinuidade no MATA030?**

O ajuste destes campos deverão ser efetuados via configurador, base de dados, editar a tabela Sa1, clicar na opção de Agrupamentos e no ícone Mover Campo, escolher o Agrupamento em que o campo está e Mover Para o Agrupamento que queira transferir.

![20220317_164555.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15370058301975)

**11 - Quais os fontes afetados na transição do MATA030 para o CRMA980?**

* MATA030
  + MATA030A
  + MATA030B
  + MATN030
  + MATN030A
  + MATS030
  + MATV030
  + MATV030A
* CRMA980  
  + CRMA980ARG
  + CRMA980BRA
  + CRMA980COL
  + CRMA980RUS
  + CRM980EventARG
  + CRM980EventARGLoj
  + CRM980EventBRA
  + CRM980EventBRAFis
  + CRM980EventCOL
  + CRM980EventDEF
  + CRM980EventDEFCrm
  + CRM980EventDEFFat
  + CRM980EventDEFFin
  + CRM980EventDEFFis
  + CRM980EventDEFGfe
  + CRM980EventDEFJur
  + CRM980EventDEFLoj
  + CRM980EventDEFOms
  + CRM980EventDEFRsk
  + CRM980EventDEFTmk
  + CRM980EventDEFTms

**12 - Onde encontro a versão atualizada do CRMA980 para implementar com a descontinuidade do MATA030?**

O pacote de expedição contínua de faturamento já contém o último fonte CRMA980: [SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)  
   
Todavia, para a mudança do CRMA980 em lugar do MATA030, não é preciso aplicar nenhum pacote para isso, será necessário apenas habilitar o parâmetro **MV\_MVCSA1**, desta forma, o o sistema já lerá o CRMA980 no cadastro do cliente.

**13 - Como é possível identificar que a rotina de cadastro de cliente esteja em MVC após ativa o parâmetro MV\_MVCSA1?**

A primeira mudança que pode ser verificada, é na stack da das rotinas do shif+f6, que a chamada do CRMA980 estará em paralelo ao MATA030.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5270300438295)

A segunda mudança é visualização de duas abas no cadastro: Principal e Informações Complementares.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5270316038423)

A  terceira mudança é posicionamento do campos que não é mais lado a lado. Existem subdivisões no cadastros para agrupar os campos de forma mais adequada:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5270436760343)

**14 - As mudanças relacionadas ao MATA030 também serão efetuadas na release 12.1.25?**

Não, as mudanças passam a valer a partir da release **12.1.27 em diante**, ou seja, **somente nos releases em vigência**, para a release 12.1.25 permanece o formato atual do cadastro de cliente por MATA030 e as as últimas atualizações datadas de DEZ/2021.

**15 - A APICarol manterá o funcionamento no CRMA980 como no MATA030?**

Sim, o funcionamento é o mesmo, não houve alterações para a tratativa de API Carol x Cadastro de clientes.

**Obs**: Caso a rotina **CRMA980** tenha sido ajustada diretamente em **menu** do Faturamento, **é necessário que se ative o parâmetro MV\_MVCSA1 para .T.** , para que haja o funcionamento adequado da API com a nova rotina nas releases **12.1.27 e 12.1.33**. Somente a partir da nova release 12.1.2210, quando não haverá mais a chamada da rotina MATA030 no menu de faturamento e sim a rotina CRMA980, que não será mais necessário a ativação do parâmetro MV\_MVCSA1.

**16 - Ao abrir o cadastro de cliente, está surgindo uma mensagem de comunicado do ciclo de vida de software, informando que o MATA030 será descontinuado em 04/04/22, o que se deve fazer?**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5277897866391)

Não precisa efetuar mudança do menu sigafat  e também não haverá nenhum pacote específico para esta mudança, o que é preciso fazer é apenas ativar o parâmetro MV\_MVCSA1 para .T. e o sistema já fará o reconhecimento da nova rotina, CRMA980 , no lugar do MATA030. Todavia, como o MATA030 não será travado, poderá permanecer na rotina para efetuar os testes na rotina nova, porém, em caso de erro no MATA030 não haverá nenhuma correção, uma vez que descontinuada, somente a nova rotina receberá correções e melhorias.

**17 - Como ficará a importação por Mile com a mudança da MATA030 para CRMA980?**

Basta ajustar o adapter para buscar a rotina CRMA980, o restante permanecerá o mesmo em relação a tabela SA1.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15370072840599)

**18 - É possível utilizar o parâmetro MV\_ENCHOLD na rotina CRMA980?**

Não é possível utilizar o parâmetro MV\_ENCHOLD na alteração da aparência do *layout*/visualização do  na rotina de cadastro do cliente (CRMA980).  **Saiba Mais**

* **[How To | MP - SIGAFAT - Rotina MATA030 Descontinuada](https://youtu.be/aEY_Xk_wnCg)**
* **[MATA030 - Cadastro de Clientes - Descontinuada em 04/04/22](https://tdn.totvs.com/x/OtMDJ)**
* **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Rotina cadastro de cliente (MATA030) descontinuada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403853592471-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Rotina-Cadastro-de-Cliente-MATA030-Descontinuada)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Tratamento de Integrações EAI após a descontinuação do Mata030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4942587681047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tratamento-de-Integra%C3%A7%C3%B5es-EAI-ap%C3%B3s-a-descontinua%C3%A7%C3%A3o-do-Mata030)**
* **[Cross Segmentos/TOTVS Backoffice (Linha Protheus)/Faturamento (SIGAFAT) - É necessária adaptação do ExecAuto MATA030 para CRMA980?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411625532567-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-%C3%89-necess%C3%A1ria-adapta%C3%A7%C3%A3o-do-ExecAuto-MATA030-para-CRMA980-)**
* **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Mile: CRMA980 (antigo MATA030)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417246157207-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mile-CRMA980-antigo-MATA030-)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Reference counter overflow ( over 32700 ) na exportação da consulta genérica da SA1 em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5099776475927-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reference-counter-overflow-over-32700-na-exporta%C3%A7%C3%A3o-da-consulta-gen%C3%A9rica-da-SA1-em-MVC)**
* **[MP - FAT - Mensagem: AO4\_CODUSR: Código de usuário não existe - Verifique o código informado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036289934-MP-FAT-Mensagem-AO4-CODUSR-C%C3%B3digo-de-usu%C3%A1rio-n%C3%A3o-existe-Verifique-o-c%C3%B3digo-informado?source=search)**
