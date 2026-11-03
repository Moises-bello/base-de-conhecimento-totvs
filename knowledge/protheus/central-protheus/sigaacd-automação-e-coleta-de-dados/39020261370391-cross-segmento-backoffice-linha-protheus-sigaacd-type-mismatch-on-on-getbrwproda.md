---
article_id: 39020261370391
category: SIGAACD - Automação e Coleta de Dados
content_hash: e2d97cc36f92fd2252fe649398c06b03a1faffc2b5464890ff78b9d699756dd7
fetched_at: '2026-06-28T22:39:13.872938+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - type mismatch on +  on
  GETBRWPROD(ACDA032.PRW)
type: support-article
updated_at: '2026-06-25T18:48:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39020261370391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-type-mismatch-on-on-GETBRWPROD-ACDA032-PRW
---

O erro "type mismatch on +" na função GETBRWPROD ocorre no Monitor de Inventário (ACDA030/ACDA032) devido à concatenação de dados incompatíveis, como descrições nulas ou caracteres especiais invisíveis em produtos. Para resolver, identifique dados corrompidos via SQL, corrija registros inconsistentes, limpe o profile do usuário e atualize o repositório SIGAACD. Caso persista, envie logs ao suporte.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39020248179607) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Ao utilizar o Monitor de Inventário (rotinas **ACDA030** / **ACDA032**), o sistema apresenta a mensagem de erro crítico: `type mismatch on +` na função `GETBRWPROD`, impedindo a exibição do browse de produtos.

**type mismatch on +  on GETBRWPROD(ACDA032.PRW) 21/01/2026 17:18:09 line : 1037**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O erro ocorre devido a uma tentativa de concatenação de tipos de dados incompatíveis no fonte `ACDA032.PRW`. Tecnicamente, a função `GETBRWPROD` tenta agrupar informações (como Produto, Descrição e Local) para montagem da grade visual. Se algum desses campos contiver um valor nulo (`NIL`), caractere de controle inválido ou tipo não caractere no banco de dados, a rotina é interrompida.

As causas principais costumam ser descrições de produtos com caracteres especiais invisíveis (provenientes de importações via Excel/Integrações) ou registros inconsistentes nas tabelas de inventário do ACD.

**Ou, caso você esteja utilizando do ponto de entrada:**  
[AC032FIL - Filtro do Monitor do Mestre de Inventário](https://tdn.totvs.com/x/GvFc)

**Identificação de Dados Corrompidos (SQL):**

1. Execute a consulta abaixo no banco de dados para identificar produtos com descrições nulas ou caracteres de controle que quebram a string de visualização, **Exemplo**:

   ```
   SELECT B1_COD, B1_DESC, R_E_C_N_O_ 
   FROM SB1010 
   WHERE B1_DESC IS NULL 
      OR B1_DESC LIKE '%' + CHAR(0) + '%' 
      OR B1_DESC LIKE '%' + CHAR(13) + '%';
   ```
2. **Verificação das Tabelas de Movimentação:**

   Valide se existem registros com campos obrigatórios em branco na tabela de itens do inventário:

   ```
   Mestre de Inventário (ACDA030 - SIGAACD)
   ```

   *Caso encontrados, os registros devem ser corrigidos via rotina ou com apoio de consultor in loc.*
3. **Limpeza de Profile do Usuário:**

   Configurações de colunas personalizadas podem forçar a leitura de índices inexistentes.

   * Acesse o módulo **Configurador (SIGACFG)**;
   * Vá em **Usuário > Senhas > Usuário**;
   * Selecione o usuário que apresenta o erro e clique em **Alterar**;
   * Clique no botão **Limpar Profile**;
   * Filtre e exclua as entradas relacionadas às rotinas **ACDA030** e **ACDA032**.
4. **Atualização de Repositório:**

   Certifique-se de que o ambiente possui o pacote de expedição contínua do módulo **SIGAACD** atualizado, garantindo que as tratativas de tratamento de nulos (`ValToChar`) estejam aplicadas ao fonte `ACDA032.PRW`.

Caso tome as ações e o erro persista, envie o log ao suporte bem como o [ID da central](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico) para validação, e informe que ja foi averiguado as condições desse artigo.

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[*SIGAACD - Quais Coletores de Dados são homologados para uso no módulo Automação e Coleta de Dados (SIGAACD)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quais-Coletores-de-Dados-s%C3%A3o-homologados-para-uso-no-m%C3%B3dulo-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-SIGAACD?source=search)  
[*Configurar impressora para impressão de etiquetas*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas)
