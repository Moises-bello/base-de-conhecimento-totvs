---
article_id: 4407692862359
category: eSocial - Tabelas/Não Periódicos
content_hash: 340e17da5b9ea8474b87875618d2a393d41012575046316fa0087197b0a72163
fetched_at: '2026-06-28T22:47:10.422140+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na geração do S-2200: Campo ''xxxxx'' do registro
  ''localTempDom'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2025-07-02T13:50:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407692862359-RH-RM-FOP-eSocial-Erro-na-gera%C3%A7%C3%A3o-do-S-2200-Campo-xxxxx-do-registro-localTempDom-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24441905743255) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Ao gerar o XML do S-2200 é apresentado erro **Campo 'xxxxx' do registro 'localTempDom' é obrigatório e não está preenchido**.

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O grupo **localTempDom** representa o **endereço de trabalho** do trabalhador doméstico e trabalhador temporário. De acordo com o Layout eSocial, esse grupo só deve ser preenchido quando a **Categoria eSocial** for igual a **104** (Empregado - Doméstico) ou **106** (Trabalhador Temporário - contrato nos termos da Lei 6.019/74).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28864125638935)

**Solução**  
Para ajuste do erro apresentado, siga os passos abaixo:

1. Edite o cadastro do funcionário e acesse o menu lateral **Informações Contratuais | Registro**;  
1.1. Verifique se o campo **Tipo de Funcionário** está corretamente preenchido como **B - Temporário com redução de encargos**, **F - Temporário/Comissionista** ou **P - Temporário**;  
1.2. Verifique se o campo Categoria eSocial está corretamente preenchido como **106 Trabalhador Temporário - contrato nos termos da Lei 6019/74**;

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407920826903)**

2. Após o preenchimento dos dados acima, acesse a aba **Trabalhador Temporário** que será exibida na parte superior da tela;  
2.1. Preencha os campos da tela, informando no campo **Empresa contratante do funcionário temporário** um cliente/fornecedor correspondente ao local onde o funcionário irá trabalhar. Se necessário, crie um cli/for com os dados da própria empesa;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407916152599)

2.2. Acesse o cliente/fornecedor informado no campo supracitado e verifique no menu lateral **Dados Gerais |** **Identificação** se o endereço principal está corretamente preenchido;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407920900759)

3. Depois de preencher os campos citados nas etapas anteriores, o XML será gerado corretamente com o grupo **localTempDom** preenchido.
