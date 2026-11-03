---
article_id: 1500003493582
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 3e947055a4cee3f7fa08c587eba2dbfc88c5f0a317c7dda3a0beebca77640a1e
fetched_at: '2026-06-28T22:40:45.629100+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - Erro I051 Duplicidade
  COD_CCUS
type: support-article
updated_at: '2023-08-22T18:13:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003493582-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Erro-I051-Duplicidade-COD-CCUS
---

**Dúvida**

Erro I051- Duplicidade COD\_CCUS

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009610661)**

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.

* **I051- Modificação de Regra**

A partir do leiaute 9 implica que uma conta contábil (I050)/centro de custo (I051) só poderá ser mapeada para uma conta referencial. Ou seja, cada centro de custo de uma conta contábil deverá corresponder a apenas uma conta referencial.

Exemplo:  
|I050|01012020|01|A|1113|111|CaixaZ  
**|I051|123|101010102** (Caixa Filial)  
**|I051|456|1.01.01.01.02**  
**|I051|789|1.01.01.01.02**

|I050|01012020|01|A|1112|111|CaixaX  
**|I051|123|1.01.01.01.02** (Caixa Filial)  
**|I051|456|1.01.01.01.02**  
**|I051|789|1.01.01.01.02**

Pode ser observado que os mesmos centros de custos **123, 456** e **789** mapeiam para o mesmo referencial, porque as contas contábeis com as quais se relacionam são diferentes.

**Por outro lado, o exemplo abaixo não é possível de ser realizado no leiaute 9:**  
|I050|01012020|01|A|1118|111|Banco  
**|I051|123|1.01.01.02.01** (Banco no País)  
**|I051|123|1.01.01.02.02** (Banco no Exterior)

Nesse caso o conjunto Conta contábil/Centro de Custo mapeia para mais de um referencial, **o que não é possível a partir do leiaute 9.**

**Solução**

Para o plano de contas (CT1) que contém o mesmo centro de custo relacionado a contas referenciais diferentes, deverá haver um ajuste nos lançamentos (CT2) referente 2020 e nova amarração do plano referencial (CVD).  Todavia, se a base possui apuração de resultados (CTBA211) deverá ser feito:

* O estorno da apuração (CTBA215)
* Os ajustes nos lançamentos (CT2) mapeando os centros de custos por conta, conforme conta referencial,  e/ou criando novos centros de custo se necessário.
* Se certificar que os saldos foram reprocessados (CTBA190)
* Apuração de resultados (CTBA211)
* Nova amarração do plano referencial (CTBA020- CVD) considerando apenas uma conta referencial por centro de custo.
* Escrituração ECD (CTBS001)

**Ainda não entendi se me enquadro nessa situação, como avaliar?**

Por exemplo, cliente envia a ECD com centro de custo.

Centro de Custo **123** é utilizados tanto em lançamentos para conta CAIXA (101010102 ) quanto para a conta de receitas (3.01.01.01.15)**.**

Ao relacionar a conta referencial, serão contas referenciais diferentes mas o mesmo centro de custo (123). Esse tipo de situação que não será mais aceita pela Receita Federal, pois a conta referencial para conta Patrimonial será uma e para a conta de Resultado será outra. Neste caso será necessário criar novos centros de custo para atender esse tipo de lançamento, ou utilizar centro de custo que já existem, porem de forma segmentada.

**O que o manual da ECD diz?**

Sobre a modificação na chave:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020050721)**

Sobre os ajustes necessários:

*"... O Balanço Patrimonial e a Demonstração do Resultado Contábil poderão ser calculados em forma definitiva (a partir da ECD, independentemente de informação fornecida na ECF), a integração entre*  
*a ECD e a ECF será facilitada e haverá diminuição da complexidade da ECF, viabilizando as metas de simplificação da escrituração.* *Em contrapartida, algumas pessoas jurídicas serão afetadas pela mudança, devendo ajustar seus centros de custo, ou gerar novos centros de custos, de modo que cada um deles corresponda a apenas uma conta referencial para fins de geração da ECD relativa ao ano-calendário 2020 a ser entregue* até maio do ano subsequente, e das escriturações posteriores."

[Manual ECD pág 41](http://sped.rfb.gov.br/pasta/show/1569)

[ECD - Modificações de Regra e da Chave do Registro I051 – Plano de Contas Referencial](http://sped.rfb.gov.br/pagina/show/5722)

**No Protheus, porque devo fazer uma nova amarração (CVD)?**

Essa nova amarração será necessária, pois essa alteração é a partir do leiaute 9. Caso seja necessário substituir a escrituração anterior, teremos que permanecer com o histórico sistêmico, conforme foi entregue na época.

**Como devo fazer a nova amarração?**

**[Cross Segmento - Backoffice Linha Protheus - CTBA020/CTBA025 Facilitador de amarração do Plano de contas com o Plano de contas Referencial (CVD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003494441-Cross-Segmento-Backoffice-Linha-Protheus-CTBA020-CTBA025-Facilitador-de-amarra%C3%A7%C3%A3o-do-Plano-de-contas-com-o-Plano-de-contas-Referencial-CVD-?source=search)**

**<https://tdn.totvs.com/display/public/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_9_00>**

**Posso ter mais de um centro de custo relacionado a mesma conta contábil?**

Sim, desde que os centro de custo mapeados para a conta referencial X não sejam os mesmo relacionados para a conta referencial Y.

Exemplo:

|I050|01012020|01|A|1113|111|CaixaZ  
**|I051|123|1.01.01.01.02** (Caixa Filial)  
**|I051|456|1.01.01.01.02**  
**|I051|789|1.01.01.01.02**

|I050|01012020|01|A|1112|111|CaixaX  
**|I051|123|1.01.01.01.02** (Caixa Filial)  
**|I051|456|1.01.01.01.02**  
**|I051|789|1.01.01.01.02**

**Importante.**

A mensagem de erro não impedirá a geração da escrituração.

Até o momento, o PGE não tem uma validação sobre essa modificação de regra.

**Saiba mais**:

* [Orientações Consultoria de Segmentos : Modificações de Regra e da Chave do Registro I051](https://tdn.totvs.com/display/public/ConSeg/ECD+-+Registro+I050+-+Plano+de+Contas+Referencial+-+Chave+do+centro+de+custos)
* [SPED modificação da chave do I051](http://sped.rfb.gov.br/pagina/show/5722)
