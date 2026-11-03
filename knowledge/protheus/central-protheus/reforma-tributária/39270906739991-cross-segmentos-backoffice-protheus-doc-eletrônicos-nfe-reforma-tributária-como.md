---
article_id: 39270906739991
category: Reforma Tributária
content_hash: f64ebad734a835a514f7bc270b8e2b6cdcdacd99d300341bd4583b49996c4d37
fetched_at: '2026-06-28T22:39:53.684146+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária
  – Como gerar a tag indDoacao
type: support-article
updated_at: '2026-03-24T21:07:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39270906739991-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Como-gerar-a-tag-indDoacao
---

**Dúvida**  
Na geração do xml do documento fiscal, o preenchimento da tag <inddoacao> deve ser feito com base na seguinte lógica: deve receber o valor “1” sempre que a operação corresponder a uma doação. Importante observar que a Nota Técnica não condiciona o uso da tag a uma única classificação tributária (cClassTrib) . Isso ocorre porque o campo foi criado justamente para orientar a apuração , independentemente do caminho tributário escolhido, seja a tributação da saída ou o estorno dos créditos vinculados.  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Para que essa informação seja gerada, é necessário que o dado adicional INDDOACAO esteja previamente cadastrado na tabela CK2 por meio do módulo de Escrita Fiscal.

        Além disso, o Perfil de Operação (FISA165) deve estar configurado com o dado adicional INDDOACAO = 1 para os perfis correspondentes a operações de doação.

        Essa configuração deve ser realizada previamente na rotina do Configurador de Tributos (FISA170), conforme orientações descritas na documentação a seguir.

<https://tdn.totvs.com.br/display/public/PROT/CFGTRIB+-+Dados+Adicionais>

        O conteúdo da tag em questão, passou a basear-se nas informações do configurador de tributos, deixando de verificar de forma fixa os códigos de classificação tributária 410003 e 410026.

         Exemplo de configuração:

![](https://tdn.totvs.com/download/attachments/1052326684/image-2026-3-19_14-25-45.png?version=1&modificationDate=1773941354473&api=v2)

![](https://tdn.totvs.com/download/attachments/1052326684/image-2026-3-19_14-26-10.png?version=1&modificationDate=1773941354160&api=v2)

![](https://tdn.totvs.com/download/attachments/1052326684/image-2026-3-19_14-26-44.png?version=1&modificationDate=1773941354073&api=v2)

![](https://tdn.totvs.com/download/attachments/1052326684/image-2026-3-19_14-27-33.png?version=1&modificationDate=1773941353937&api=v2)

![](https://tdn.totvs.com/download/attachments/1052326684/image-2026-3-19_14-28-2.png?version=1&modificationDate=1773941353877&api=v2)

Realize as atualizações abaixo no Protheus:  
DSERTAF4-3186  
12.1.2210:<https://r.totvs.io/p/1240231> ; 12.1.2310:<https://r.totvs.io/p/1240232> ; 12.1.2410:<https://r.totvs.io/p/1240229> ; 12.1.2510:<https://r.totvs.io/p/1240230>

 DSERFIS4-3139  
12.1.2210:<https://r.totvs.io/p/1243077> ; 12.1.2310:<https://r.totvs.io/p/1243078> ; 12.1.2410:<https://r.totvs.io/p/1243079> ; 12.1.2510:<https://r.totvs.io/p/1243076> ;  
   
Aplique o fonte NFESEFAZ padrão abaixo que consta no pacote:  
<https://suporte.totvs.com/portal/p/10098/download?e=1152113>

Obs: Caso tenha duvidas no processo entrar em contato com suporte Fiscal.
