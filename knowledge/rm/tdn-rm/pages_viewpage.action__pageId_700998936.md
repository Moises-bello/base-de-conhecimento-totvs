---
content_hash: 1d0eed3e8ed3f9248ac24e8134db3bea1871448a881fa5a158ae984344adc5a5
fetched_at: '2026-06-29T00:11:22.254697+00:00'
page_id: '700998936'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - Transferir Contratos de
  Venda TIN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=700998936
version: 8
---

Importante:

O objetivo de se transferir de contratos entre coligadas é tratar os casos de fusão ou cisão de empresas, onde os contratos que estavam sendo tratados por uma empresa devem passar a ser tratados por outra empresa do grupo.

Através desta funcionalidade será possível copiar os contratos de venda do TIN de uma coligada para outra, juntamente dos lançamentos financeiros. Ao termino do processo os **contratos** e as **subunidades**(Disponíveis para venda) serão **bloqueados** na coligada de origem.

Para executar o processo, é necessário acessar a aba '**Utilitários**' e posteriormente clicar na opção '**Transferir Contratos de Venda TIN**':

**É necessário informar os seguintes dados:**

Selecionando os campos:

**Coligada de Origem**: Obrigatório selecionar a Coligada Origem a partir da qual este processo irá buscar os Contratos a serem transferidos.

**Empreendimento de Origem**:

O Preenchimento desta informação não é necessário, tendo o mesmo o seguinte comportamento:

* Ao informar um Empreendimento: serão transferidos os dados financeiros e os dados do TCGI entre a Coligada Origem e Coligada de Destino.
* Caso não seja informado nenhum Empreendimento: serão transferidos os dados de TODOS os empreendimentos da Coligada.

**Coligada Destino** : Coligada para qual os Contratos tratados neste processo serão transferidos.

**Conta Caixa de Destino** : Informar a conta caixa de destino, **que será utilizada apenas para fazer essa transição** entre as baixas originadas na Coligada Origem e a Coligada de Destino, para que as Baixa antigas não interfiram contábil e fiscalmente na Coligada de Destino.

As *Parcelas Baixadas* terão essa informação de Conta Caixa de Transição atualizadas nas Tabelas: FXCX, FXCXHST, FLANBAIXA e FLANBAIXAHST.

Para as *Parcelas em Aberto* a Conta Caixa associada permanecerá a mesma da Coligada de Origem, que serão recriadas na a Coligada de Destino.

Posteriormente, essas Parcelas poderão ter a sua Conta Caixa trocadas por uma nova Conta, manualmente.

Cabe ainda ressaltar, que não serão atualizados nenhum Saldo dessas Contas automaticamente.

Parâmetros:

* **Desativar os Contratos / Empreendimentos da coligada de origem :** Desativa os contratos , os deixando bloqueados na coligada de Origem.
* **Copiar todos os Parâmetros do TCGI e Financeiro :** Marcando esse parâmetros , todos parâmetros do TCGI e Financeiro , serão copiados para a nova coligada.
* **Copiar todo o histórico do TIN e Financeiro:** Serão copiados todos os dados das tabelas de logs, caso esteja desmarcado será copiado somente o último log de cada parcela.

Atenção:

**O Processo é irreversível. Antes de realizar a execução faça um backup da base de dados.**

**Importante:**

As baixas que vieram da coligada origem, terão a **Conta Caixa** que foi determinada no processo.

O status contábil de todas as baixas estarão como "**Não contábil**".

Os lançamentos financeiros baixados na coligada Destino, serão bloqueadas pelo Tipo "**Importação de Sistema Legado**".

Os Boletos que estejam em aberto(**Registrado** ou  **Não Registrado**) na coligada de Origem serão cancelados é será criado um novo boleto na coligada de Destino. Este novo Boleto que será criado irá manter o Status CNAB do boleto de Origem.

O sistema irá **Bloquear** automaticamente na coligada de origem apenas os contratos que permitem essa ação, caso seja apresentado alguma consistência que não permita a conclusão da operação será necessário uma analise do usuário e posteriormente um bloqueio manual.

Processo ao ser executado , mostra as tabelas que estão sendo feita as transferências.

Importante:

Caso o usuário não consiga acesso para Coligada destino , fazer o procedimento abaixo.

Selecionar a Coligada , Processo | Incluir usuário supervisor nso Módulos.

Perfil com Coligada associada.

Contratos do Empreendimento encontram-se Bloqueados na coligda Origem.

Imagem mostra contratos na Coligada 1 e depois na nova Coligada.

INTEGRAÇÃO PROTHEUS

## **Integração com o Protheus EAI - 2**

Após copiar os dados da linha RM, favor executar o processo '**Enviar Copia de Coligada**' para copiar as parcelas que estão em abertos e parcialmente baixadas no RM e enviar para o Protheus
