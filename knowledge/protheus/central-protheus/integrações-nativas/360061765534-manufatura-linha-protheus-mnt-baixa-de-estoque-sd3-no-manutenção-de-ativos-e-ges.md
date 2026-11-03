---
article_id: 360061765534
category: Integrações Nativas
content_hash: 3f513065248313ee42cfabdf35463f83989166b3c160578b3a3eac05f7309efc
fetched_at: '2026-06-28T22:42:35.340259+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Baixa de Estoque SD3 no Manutenção de Ativos
  e Gestão de Frotas
type: support-article
updated_at: '2024-10-25T17:50:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061765534-Manufatura-Linha-Protheus-MNT-Baixa-de-Estoque-SD3-no-Manuten%C3%A7%C3%A3o-de-Ativos-e-Gest%C3%A3o-de-Frotas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:03:15 min****Dúvida**Como funciona a **B****aixa** **de Estoque** na tabela **SD3 - Movimentos Internos** no **Manutenção de Ativos** e **Gestão de Frotas** pela rotina **Retorno Mod. 2 - MNTA435**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**Para realização da baixa de **Estoque** são necessários os passos abaixo:

1. Acessar o **Configurador - SIGACFG**;
2. Ir em **Ambiente / Cadastros / Parâmetros - CFGX017**;
3. Configurar os parâmetros:  
   **MV\_NGMNTES - Integração Manutenção com Estoque** igual a **S - Sim**   
   **MV\_NGGERSA - Indica se deve gerar Solicitação de Armazém ao invés de gerar Solicitação de Compras** igual a **N - Não**   
   **MV\_ESTNEG - Identifica se o Sistema permitirá saldos em estoque negativo** igual a **S - Sim**.  Caso seja igual a **N - Não**, deverá ser incluso saldo para o produto no **Estoque**;
4. O motivo da geração de **Solicitação de Armazém - S.A** estar desabilitada, se dá pelo fato de que a baixa de **S.A** será controlada pelo módulo de **Estoque - SIGAEST**;
5. Acessar o **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**;
6. Ir em **Atualizações / Controle de Oficina / Cadastros Básicos / Produtos - MATA010** e cadastrar um **Produto** que será utilizado como **insumo previsto**;
7. Ir em **Atualizações / Controle de Oficina / Manutenção / Serviços - MNTA040** e cadastrar um **Serviço - MNTA040** do tipo **Corretivo**;
8. Ir em **Atualizações / Controle de Oficina / Bens / Bens - MNTA080** e cadastrar um **bem**;
9. Ir em **Atualizações / Controle de Oficina / Ordem de Serviço / Corretiva - MNTA420** e incluir uma **O.S. - Ordem de Serviço**, informando o **Produto** como **insumo previsto**, o **Serviço** e o **Bem** cadastrados anteriormente;
10. Ir em **Atualizações / Controle de Oficina / Retorno de Ordem de Serviço - O.S. / Retorno mod. 2 - MNTA435**, selecionar a **O.S.** cadastrada anteriormente;
11. Verificar que o **insumo** reportado no passo **9** está na *label* de **Insumos Previstos**, selecionar o **Produto** e clicar em **Incluir o insumo previsto**;
12. Verificar que o **produto** passa para a *label* de **Insumos realizados**;
13. Clique em **Salvar** e o **Manutenção de Ativos** movimentará a **SD3** com o campo **D3\_CF - Tipo de Requisição/Devolução** igual a **RE0**.

Para melhor entendimento, segue um detalhamento do processo desde a criação de **Ordem de Serviço** até o momento da movimentação do **Estoque**:

* Abertura da **Ordem de Serviço Corretiva**:Ao acessar a rotina **MNTA420**, inclua uma **O.S**. informando um **bem** e na pasta **Insumos**, um insumos previsto do tipo **Produto**.

| Código | Bem | Insumo Previsto | Quantidade |
| --- | --- | --- | --- |
| 000001 | CARRO001 | Peça 001 | 01 |

Aqui geramos a **Ordem de Serviço** e estamos prevendo que será utilizada a **Peça 001** para realizar a manutenção do bem **CARRO001**;

* Aplicação do **Insumo Previsto** na **Ordem de Serviço**:Ao acessar a rotina **MNTA435**, filtre e selecione a **Ordem de Serviço** incluída anteriormente. Ao selecionar a **O.S**., o Sistema apresenta o **Insumo Previsto** incluso na rotina de **MNTA420**, sendo assim possível **Realizar** esse **insumo**, ou seja, aplicar ele para que seja possível realizar a baixa no **Estoque** na tabela **SD3**, para isso basta clicar duas vezes em cima da linha do **insumo previsto** e selecionar a opção **Incluir o insumo previsto** e em seguida **Salvar** as alterações ou **Confirmar** a rotina, conforme tabela abaixo.

| O.S. | Bem | Insumo Previsto | Insumo Realizado | Quantidade | SD3 |
| --- | --- | --- | --- | --- | --- |
| 000001 | CARRO001 | Peça 001 | Peça 001 | 01 | RE0 (baixa) |
