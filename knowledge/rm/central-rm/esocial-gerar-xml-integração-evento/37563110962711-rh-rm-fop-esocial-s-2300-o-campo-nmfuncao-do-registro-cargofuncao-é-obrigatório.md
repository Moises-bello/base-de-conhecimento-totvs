---
article_id: 37563110962711
category: eSocial - Gerar XML/ Integração Evento
content_hash: 08f9f797f3f378a946c9b9aa038f2fd775d87025d2a61c78ac31aaf7928dcb92
fetched_at: '2026-06-28T22:47:13.171794+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-2300 - O campo 'nmFuncao' do registro 'cargoFuncao'
  é obrigatório e não está preenchido.
type: support-article
updated_at: '2026-04-17T18:07:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37563110962711-RH-RM-FOP-eSocial-S-2300-O-campo-nmFuncao-do-registro-cargoFuncao-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37563156941079) Tempo aproximado para leitura: 00**:**20:00 min  
  
**Ocorrência**  
Ao gerar o XML do **evento S-2300 (Trabalhador Sem Vínculo)**, o sistema apresenta erro de validação e o arquivo não é transmitido ao eSocial. Erro o campo ‘nmFuncao’ do registro ‘cargoFuncao’ é obrigatório e não está preenchido.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre quando: A flag **“Possui Função de Confiança/Cargo em Comissão”** está marcada no cadastro do trabalhador sem vínculo; o **campo Função de Confiança** não está preenchido **ou n**ão existe **histórico de função de confiança** com data inicial compatível com o início do trabalhador sem vínculo.  
  
**Solução**  
**Validar o cadastro do trabalhador sem vínculo**

1. Acesse:  
   **Cadastros > Trabalhador Sem Vínculo > Aba Registro**
2. Verifique se a flag **“Possui Função de Confiança/Cargo em Comissão”** está marcada.
3. Caso esteja marcada:

![image.png](https://totvssuporte.zendesk.com/attachments/token/on3FOBT7HwGG6Sc7DnSpsslOd/?name=image.png&lotus_request=true)

* Preencha corretamente o campo **Função de Confiança**, selecionando uma função válida.

  ⚠️ Se o trabalhador **não exerce função de confiança**, desmarque essa flag e salve o cadastro.

**Validar o cadastro da Função**

1. Acesse:  
   **Cadastros > Funções**
2. Abra a função informada no trabalhador.
3. Na aba **eSocial**, verifique se **NÃO** está marcada indevidamente a opção:

![image.png](https://totvssuporte.zendesk.com/attachments/token/rRsSSqsAFR4OLKKt9jvUM9DZo/?name=image.png&lotus_request=true)

**“Considerar como Função de Confiança/Cargo em Comissão”**, caso não seja aplicável.

**Validar o Histórico de Função de Confiança**

1. Acesse o cadastro do trabalhador sem vínculo.
2. Clique em:  
   **Anexos > Históricos > Histórico Função de Confiança/Cargo em Comissão**

![image.png](https://totvssuporte.zendesk.com/attachments/token/KHp4einOFbtuMn9VXIWiVZFUD/?name=image.png&lotus_request=true)

Verifique se existe um registro:

* Com **Data Inicial da Mudança** igual ou anterior à data de início do trabalhador sem vínculo;
* Com a **Função de Confiança preenchida**.

 Caso não exista, inclua o histórico corretamente.

Após o preenchimento correto da **Função de Confiança** e do respectivo **histórico**, o XML do **S-2300** será gerado corretamente, contendo a tag `nmFuncao`, e o evento poderá ser transmitido ao eSocial sem erros.

[RH - RM - FOP - eSocial - Utilização do evento S-2300 - Trabalhador Sem Vínculo do Emprego / Estatutário - Início](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015286312-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-evento-S-2300-Trabalhador-Sem-V%C3%ADnculo-do-Emprego-Estatut%C3%A1rio-In%C3%ADcio)
