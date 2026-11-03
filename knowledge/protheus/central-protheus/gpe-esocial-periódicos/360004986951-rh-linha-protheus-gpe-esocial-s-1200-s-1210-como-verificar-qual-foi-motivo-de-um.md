---
article_id: 360004986951
category: GPE - eSocial - Periódicos
content_hash: 7ba9da849d30543716d531fb0f28a1ccb761c6e5b7646569e347958a4d5e12b1
fetched_at: '2026-06-28T22:45:07.334042+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 / S-1210 - Como verificar qual
  foi motivo de uma verba ou valor não ser gerado no evento S-1200 ou S-1210?
type: support-article
updated_at: '2021-04-13T16:37:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004986951-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-verificar-qual-foi-motivo-de-uma-verba-ou-valor-n%C3%A3o-ser-gerado-no-evento-S-1200-ou-S-1210
---

**Dúvida**Como verificar qual foi motivo de uma verba ou valor não ser gerado no evento S-1200 ou S-1210?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - TAF - A partir da versão 11.80

**Solução**Existe situações onde verbas / valores da folha não são geradas nos eventos S-1200 ou S-1210., isso porque no eSocial existe validações especificas para cada situação, com isso quando a natureza ou incidência não atende a regra do esocial o sistema pode não gerar a informação.

Para descobrir o motivo é necessário fazer uma analise previa no layout do esocial, pois pode ocorrer das verbas não estarem cadastradas conforme as regras de validação do evento.

As premissas para essa analise são:

* Descobrir a TAG do esocial que deve se gerar o registro correto;
* Entender a regra de validação da TAG no esocial;
* Verificar se a configuração no sistema atender a regra do esocial.

**Abaixo é possível ver um exemplo de analise que pode ser utilizado para verificação de problemas encontrados na geração dos eventos.**

**1. Como localizar qual a tag no layout do esocial?**

Verifique o nome do campo acessando a rotina como alterar e apertando a tecla F1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006453351/mceclip0.png)

a) Acesse o link Eventos S-1200 De / Para de campos Protheus com layout eSocial: <http://tdn.totvs.com/x/pf8TEQ>  
b) Localize o mesmo campo na FAQ abaixo (**C9M\_CODRUB**)  
c) Conforme imagem O campo **C9M\_CODRUB** no TAF representa a TAG **codRubr**no layout do esocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006453371/mceclip1.png)

d) Acesse o Leiautes do eSocial v2.4.02.pdfl: <https://portal.esocial.gov.br/institucional/documentacao-tecnica>  
e) Clique no S-1200 no índice.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006453411/mceclip2.png)

f) No S-1200 localize o grupo itensRemun tag **codRubr**e verifique as regras para geração das informações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006416272/mceclip3.png)

**2. Como analisar a Tag no layout do esocial?****Após localizar a tag no layout verifique as regras de validação.**

Tag **codRubr**

Grupo **itensRemun**

**Regras de Validação:**

Informar o código atribuído pelo empregador e que identifica a rubrica em sua folha de pagamento.

O código informado deve existir na tabela S-1010 - Tabela de Rubricas, vigente no período indicado em:

a) {perApur} se vinculado a {remunPerApur};

b) {perRef} se vinculado a {remunPerAnt}.

Não pode ser utilizada rubrica:

a) cujo {codIncCP} em S-1010 seja igual a **[23, 24, 61**];

b) cujo {codIncIRRF} em S-1010 seja igual a [**31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82, 83**];

c) cujo {codIncCp} em S-1010 seja igual a [**25, 26, 51**] se {codCateg} pertencer a um dos grupos 'contribuinte individual' ou 'bolsistas' da Tabela 01 (Categoria de Trabalhadores).

Conforme regra de validação do esocial não deve ser utilizada **rubricas** onde campo **codIncIRRF** e **codIncCP**seja igual as opções acima. Ou seja rubricas que estão nesse cenário não deve ser gerado para o esocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006453431/mceclip4.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006453451/mceclip5.png)

**3. Onde verificar as rubrica no SIGAGPE?****Acesse o cadastro de verbas na aba esocial**

E localize as informações nos campos:

* Natureza = **natRubr**
* Cd. Inc. IRRF =**codIncIRRF**
* Cd. Inc FGTS = **codIncFGTS**
* Cd. Inc Sind = **codIncSIND**
* Cd. Inc CP = **codIncCP**

No caso do exemplo os campos **codIncIRRF** e **codIncCP** estão atendendo as regras para geração do evento **S1200**.

**Observação:** quando realizada a alteração de alguma verba deve ser enviado o evento S-1010 e depois gerar o S1200 / S1210 novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006453491/mceclip6.png)

**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)   
[Chatbot eSocial](https://chat-app.meudroz.com/#/prechat?header=false&token=dG90dnMtdXNlci0yOkFrVGllLDIwMTck&customerKey=totvs&openDelay=0&typingDelay=2500&watsontoken=false&watsonuser=false&watsonurl=false)
