---
content_hash: 1b9ba7e08064da593aab553d538f56f8510d96a98f9b0fa38b95059116007122
fetched_at: '2026-06-29T00:10:30.095799+00:00'
page_id: '519195400'
product: rm
source: tdn-rm
title: Utilitários - Transferir Contratos de Venda entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519195400
version: 2
---

Através desta funcionalidade será possível copiar os contratos de venda do TIN de uma coligada para outra, juntamente dos lançamentos financeiros. Ao termino do processo os **contratos** e as **subunidades**(Disponíveis para venda) serão **bloqueados** na coligada de origem.

Para executar o processo, é necessário acessar a aba '**Utilitários**' e posteriormente clicar na opção '**Transferir Contratos de Venda TIN**':

**É necessário informar os seguintes dados:**

* **Coligada de Origem:** De onde serão  buscados os contratos.
* **Coligada Destino:** Para onde vão os novos contratos e seus lançamentos.
* **Conta caixa Destino:** Onde serão registradas as baixas que foram feitas na coligada origem.
* **Copiar todo o histórico do TIN e Financeiro:** Serão copiados todos os dados das tabelas de logs, caso esteja desmarcado será copiado somente o último log de cada parcela.

Atenção:

**O Processo é irreversível. Antes de realizar a execução faça um backup da base de dados.**

**Importante:**

1. As baixas que vieram da coligada origem, terão a **Conta Caixa** que foi determinada no processo.

        1.2  A **Conta Caixa deve ser exclusiva para essa transferência**, para que toda movimentação seja isolada nesta conta caixa, já que as baixas ocorreram realmente na coligada de origem e não na de destino;

        2. O status contábil de todas as baixas estarão como "**Não contábil**".

        3. Os lançamentos financeiros baixados na coligada Destino, serão bloqueadas pelo Tipo "**Importação de Sistema Legado**".

        4. Os Boletos que estejam em aberto(**Registrado** ou  **Não Registrado**) na coligada de Origem serão cancelados é será criado um novo boleto na coligada de Destino. Este novo Boleto que será criado irá manter o Status CNAB do boleto de Origem.  
        4.1  Sobre Envio de Títulos Remetidos ( RM para o Protheus ) Lançamentos gerados pela cópia de contrato que já contem boletos e encontram-se remetidos apenas no RM e não no Protheus .. >> Processo que deixa os mesmos remetidos no Protheus  [( Clique Aqui )](https://tdn.totvs.com/pages/viewpage.action?pageId=516641108).

        5. O sistema irá **Bloquear** automaticamente na coligada de origem apenas os contratos que permitem essa ação, caso seja apresentado alguma consistência que não permita a conclusão da operação será necessário uma analise do usuário e posteriormente um bloqueio manual.

# Em caso de Integração com Protheus EAI - 2

Após copiar os dados da linha RM, favor executar o processo '**Enviar Copia de Coligada**' para copiar as parcelas que estão em abertos e parcialmente baixadas no RM e enviar para o Protheus
