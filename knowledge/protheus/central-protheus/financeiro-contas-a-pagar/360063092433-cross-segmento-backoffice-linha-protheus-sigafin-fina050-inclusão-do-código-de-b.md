---
article_id: 360063092433
category: Financeiro - Contas a Pagar
content_hash: 82a2241622d1f931759630c4b46851d8a8382cf72b86db32e47ea611669ae2d9
fetched_at: '2026-06-28T22:38:08.211707+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Inclusão do
  Código de Barra - HELP INVCDBAR
type: support-article
updated_at: '2022-08-22T14:13:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063092433-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Inclus%C3%A3o-do-C%C3%B3digo-de-Barra-HELP-INVCDBAR
---

**Ocorrência**No módulo Financeiro FINA050, ao tentar realizar o incluir código de barras é informado que o código de barras é invalido.   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103642173/mceclip0.png)  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – FINA050 - Todas versões  
  
**Causa**Esse incidente informado INVCDBAR, ocorre devido a não ser validado o código informado campo E2\_CODBAR  
  
**Solução**Para que o erro não ocorra deve-se carregar os campos corretamente, ou seja código de barras **E2\_CODBAR** e linha digitável no **E2\_LINDIG.**

Caso tenho duvida se trata de linha digitavel ou Código de barras, poderá ser verificado pela quantidade de caracteres.  Os dados da Linha Digitável representam o conteúdo do Código de Barras dispostos em outra ordem e acrescidos de dígitos verificadores nos 3 primeiros campos onde:

**E2\_CODBAR** Código de Barras tem 44 dígitos

**E2\_LINDIG**  Linha Digitável tem 47 dígitos

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411196432407/mceclip0.png)

E ainda pode ser utilizado na rotina FINA050 / FINA750 - *Outras Ações* - *Código de Barras*, onde inserindo código valido o sistema automaticamente distribui para o campo correto (**E2\_CODBAR** e **E2\_LINDIG )**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411203557271/mceclip1.png)**

Essa função já esta disponível desde Fevereiro/2021, caso não apareça a opção ( *Outras Ações* - *Código de Barra)* será necessário do atualização da rotina (**FINA050**) e do dicionário de dados  na qual disponibilizadas novas funcionalidades entre elas, preenchimento automático (*Outras Ações* - *Código de Barra )*

Para habilitar essa funcionalidade será necessário além do pacote aplicado **(ATUALIZACAO\_FIN\_EXPEDICAO\_CONTINUA**) também o dicionário contido nesse pacote ( SXSBRA.TXT ) através do **UPDDISTR**.

**Importante**Pacote disponível para habilitação das funcionalidade mencionadas **FINANCEIRO**

ACUMULADO - 12.1.27 - <https://suporte.totvs.com/portal/p/10098/download?e=954746>  
ACUMULADO - 12.1.33 <https://suporte.totvs.com/portal/p/10098/download?e=1039087>

**Saiba mais**[DESCRICAO\_CAMPOS\_E2\_LINDIG\_E\_E2\_CODBAR](https://tdn.totvs.com/display/PROT/FIN0052_DESCRICAO_CAMPOS_E2_LINDIG_E_E2_CODBAR)
