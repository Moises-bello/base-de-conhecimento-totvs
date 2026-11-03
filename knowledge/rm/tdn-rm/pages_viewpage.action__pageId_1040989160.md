---
content_hash: 9ce0fd7d93703ee6e5fbea13bb9dffa13aae5783d87a21d76021c8eae3cace94
fetched_at: '2026-06-29T00:05:49.638813+00:00'
page_id: '1040989160'
product: rm
source: tdn-rm
title: Novo Padrão de CNPJ Alfanumérico RM Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1040989160
version: 2
---

Pré-requisito Obrigatório!

O correto funcionamento do novo padrão de CNPJ no RM Saúde depende da atualização do **RM** para o patch mais recente da **12.1.2506 e releases acima.**

## **CONTEÚDO**

2CONTEÚDO

## **01. Visão Geral**

A Receita Federal publicou a Instrução Normativa nº 2.229/2024, que altera o formato do CNPJ. A partir de **julho de 2026**, os novos CNPJs poderão conter **letras e números**, mantendo o mesmo tamanho de 14 caracteres.

O TOTVS Gestão Hospitalar foi ajustado para aceitar esse novo formato, garantindo que você possa continuar cadastrando prestadores, convênios e responsáveis financeiros sem nenhum problema.

## **02. Principais Mudanças**

### Como era antes:

* + CNPJ com apenas números: `12.345.678/0001-90`
  + 14 posições numéricas

### O que muda:

* + CNPJ pode ter letras e números: 12.ABC.345/01DE-35
  + As **12 primeiras posições** podem ter letras • Os **2 últimos dígitos** continuam sendo apenas números • CNPJs antigos **continuam válidos**

## **03. Prazo de Adequação**

Importante! Integração EAI 1.0

O novo padrão de CNPJ alfanumérico **não terá suporte na integração EAI 1.0**. Esta integração foi descontinuada conforme comunicado oficial de ciclo de vida da TOTVS.

Se você utiliza a integração com Backoffice (DATASUL ou PROTHEUS) através do EAI 1.0, será necessário realizar a transição para a **integração iPaaS** antes de julho de 2026.

Para mais informações sobre a descontinuação e o processo de migração, consulte o [comunicado oficial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34676056611863-Descontinua%C3%A7%C3%A3o-da-Integra%C3%A7%C3%A3o-com-Backoffice-DATASUL-e-PROTHEUS-via-EAI-1-0-vertical-de-sa%C3%BAde) ou entre em contato com seu ESN para realizar a transição.

**Quando a mudança entra em vigor:**

* + A Receita Federal começará a emitir CNPJs com o novo formato a partir de **julho de 2026**.

**Quando o sistema estará preparado:**

* + A versão **12.1.2602** já está preparada para o novo formato.
  + A versão **12.1.2510** estará disponível em patch até o final de abril de 2026.

**O que você precisa fazer:**

* + Atualizar o sistema antes de julho de 2026.
  + Validar se os cadastros de prestadores, convênios e responsáveis estão corretos.
  + Caso trabalhe com operadoras ou sistemas externos, confirmar se eles também estão preparados.

## **04. Ajustes Realizados no Sistema**

Importante! Padrão TISS

Somente o padrão **TISS 4.03.00** suporta o envio de CNPJ alfanumérico nos arquivos XML de faturamento para operadoras.

Se você utiliza versões anteriores do TISS (3.05.01, 3.05.02, 4.01.00, 4.02.02), será necessário atualizar para a versão 4.03.00 antes de julho de 2026 para garantir o correto envio de CNPJs com letras.

Para mais informações sobre a atualização do padrão TISS, consulte a documentação específica ou entre em contato com o suporte.

O sistema foi ajustado em todas as telas e processos que utilizam CNPJ, garantindo que o novo formato seja aceito automaticamente.

### Como funciona a validação:

* + O sistema valida automaticamente se o CNPJ informado é válido, seja ele no formato antigo (apenas números) ou no novo formato (com letras).
  + Se o CNPJ estiver incorreto, você verá uma mensagem informando que o documento é inválido.

### Onde o sistema foi ajustado:

**Cadastros:**

* + Cadastro de prestadores
  + Cadastro de convênios
  + Cadastro de responsáveis financeiros
  + Cadastro de fornecedores

**Atendimento:**

* + Agenda de atendimentos
  + Registro de atendimento (responsável financeiro)

**Faturamento:**

* + Gestão de repasse
  + Solicitação de nota fiscal

**SUS:**

* + Processamento de arquivos (AIH, BPA, APAC)
  + Lançamentos BPA
  + Procedimentos realizados

**Faturamento TISS:**

* + Geração de arquivos XML no padrão TISS 4.03.00

## **05. O que Muda para Você**

### Durante o cadastro:

**Antes:** Você digitava apenas números no campo de CNPJ.

**Agora:** Você pode digitar números e letras. O sistema aplica a máscara automaticamente.

**Exemplo:** Se você digitar `12ABC34501DE35`, o sistema formata para `12.ABC.345/01DE-35`

### Validação automática:

Quando você salvar o cadastro, o sistema verifica se o CNPJ é válido. Se estiver incorreto, uma mensagem será exibida e você não conseguirá prosseguir até corrigir.

### CNPJs antigos:

Os CNPJs que você já tem cadastrados **continuam funcionando normalmente**. Você não precisa fazer nada com eles.

### CPF:

Nada muda na validação de CPF. Tudo continua funcionando como antes.

## **06. Dúvidas Frequentes**

**1. Os CNPJs que já tenho cadastrados vão parar de funcionar?**

Não. Todos os CNPJs antigos continuam válidos e funcionando normalmente.

---

**2. Preciso recadastrar os CNPJs que já existem no sistema?**

Não. O sistema foi preparado para aceitar tanto o formato antigo quanto o novo. Você não precisa fazer nada.

---

**3. Quando vou começar a ver CNPJs com letras?**

A partir de julho de 2026, quando a Receita Federal começar a emitir CNPJs no novo formato.

---

**4. O sistema já aceita CNPJ com letras?**

Sim, a partir das versões 12.1.2510 e 12.1.2602, que estarão disponíveis em maio de 2026.

---

**5. E se eu trabalhar com uma operadora que ainda não atualizou o sistema dela?**

Você precisará confirmar com a operadora se o sistema dela já está preparado para o novo formato. O TOTVS Gestão Hospitalar já está pronto, mas a integração depende dos dois lados.

---

**6. Uso o padrão TISS para faturamento. Preciso fazer alguma atualização?**

Sim. Somente o padrão **TISS 4.03.00** suporta CNPJ alfanumérico. Se você ainda utiliza versões anteriores (3.05.01, 3.05.02, 4.01.00, 4.02.02), será necessário atualizar para a 4.03.00 antes de julho de 2026.

---

**7. Como sei se um CNPJ é válido?**

O sistema valida automaticamente no momento em que você tenta salvar o cadastro. Se o CNPJ estiver errado, você verá uma mensagem de erro.

---

**8. Posso ter CNPJs antigos e novos cadastrados ao mesmo tempo?**

Sim. O sistema aceita e valida os dois formatos sem nenhum problema.
