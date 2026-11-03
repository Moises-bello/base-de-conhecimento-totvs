---
article_id: 26509815586711
category: RH - Contabilização
content_hash: fde6235fc29402164ca2f1b3d22d77b17c6de36cc8d2bb806dc2dc5e3eaa64af
fetched_at: '2026-06-28T22:43:45.807124+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como Contabilizar a Baixa de Transferência de 1ª
  Parcela do 13º Salário na Provisão
type: support-article
updated_at: '2025-07-17T13:10:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26509815586711-RH-Linha-Protheus-GPE-Como-Contabilizar-a-Baixa-de-Transfer%C3%AAncia-de-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-na-Provis%C3%A3o
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26509811472151) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como Contabilizar a Baixa de Transferência de 1ª Parcela do 13º Salário na Provisão da Lotação Origem, para funcionários com Transferência no mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - À Partir da Versão 12.

**Solução**Foi Criado o Identificador de Cálculo 1964 que possibilita a baixa da primeira parcela do 13º salário por transferência.  
**Importante:** O identificador de cálculo não será obrigatório, e caso não seja cadastrado, a baixa da primeira parcela não será realizada.

1. Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040) e clique em Incluir.  
  
2. Inclua uma nova verba atrelando o Identificador de Cálculo 1964, como no exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26509815560215)  
  
3. Para que esta verba seja Contabilizada, será necessário atrelar um Lançamento Padrão no campo "Lcto. Padrão" (RV\_LCTOP) na aba Contabilização do cadastro da verba:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26509815562519)

**Observação:** A verba deve ser incluída como **Base Provento** no campo "Tipo do Cod." (RV\_TIPOCOD), e não há obrigatoriedade de preenchimento da aba Incidências, tendo em vista que esta verba não tem nenhuma tributação.  
  
4. Após finalizar o cadastro, clique em Confirmar.  
  
5. Ao processar as provisões para funcionários com Transferência, e que já receberam a antecipação da 1ª parcela do 13º salário, a verba com identificador 1964 será calculada na Filial, Centro de Custo, Item Contábil ou Classe Valor Origem.  
  
**Exemplo**Funcionário teve 50% do 13º Salário antecipado no mês 06/2024 e Transferência em 01/07/2024, do Centro de Custo 000000010 para o Centro de Custo 000000022.  
  
No Centro de Custo Origem com Tipo de Movimento 5 (000000010), será gerada a verba com id 1964 com o valor da antecipação do 13º salário, e a verba será contabilizada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26509811474327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26509811475735)

**Saiba Mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=866530884>

[RH-Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
