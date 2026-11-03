---
content_hash: 703efa74ba57cd934305e649d77c15783272b8bf2cf8e2f2eafe25c73610629b
fetched_at: '2026-06-29T00:09:15.492072+00:00'
page_id: '421385392'
product: rm
source: tdn-rm
title: Motivos de Improdutividade
type: documentation
url: https://tdn.totvs.com/display/LRM/Motivos+de+Improdutividade
version: 21
---

---

Este cadastro é utilizado no TOTVS Construção Obras e Projetos para definição dos motivos de improdutividade. Os motivos de improdutividade são informados nos apontamentos e apropriações de horas improdutivas, tanto para recursos de mão de obra quanto para equipamentos.

Para acessar esse cadastro, é necessário ter permissão no perfil, conforme destacado abaixo:

Quando integrado com o Manutenção de Ativos (SIGAMNT), somente será possível inserir/excluir/editar os registros que são do tipo mão de obra. Os registros de equipamento estarão bloqueados, pois são provenientes da integração/sincronização com o Manutenção de Ativos.

Acessando o TOTVS Construção Obras e Projetos, é possível visualizar esses registros no menu Cadastros Gerais > Motivo de Improdutividade:

Nos apontamentos de Mão de Obra e Equipamentos provenientes do coletor móvel, quando nenhum motivo de improdutividade é informado, temos um apontamento produtivo, já quando é selecionado algum motivo de improdutividade, o apontamento é considerado improdutivo.

Logo abaixo, é possível ver a tela de cadastro do Motivo de Improdutividade:

Os campos em negrito na tela acima, são obrigatórios no cadastro de um Motivo de Improdutividade, abaixo, todos estão listados e detalhados:

* **Tipo:** Indica se o Motivo de Improdutividade será usado para apontamentos de Equipamento ou Mão de Obra;
* **Código:** Código para identificação do Motivo;
* **Descrição:** Breve descrição do Motivo de Improdutividade;
* **Improdutividade de Mão de Obra Associada:** Motivo de improdutividade de mão de obra que será associado aos apontamentos improdutivos dos operadores dos equipamentos;
* **Status para Monitoramento:** Status para monitoramento da improdutividade, é exibido no  (tanto para Equipamento quanto Mão de Obra), onde mostrará o total de funcionários/equipamentos improdutivos, agrupados pelo Status para Monitoramento dos Motivos de Improdutividade cadastrados. Ex.: (Normal, Alta e Crítica).

Abaixo é possível visualizar os dois monitores; em destaque, o monitoramento pelo Status cadastrado no Motivo de Improdutividade, informado nos apontamentos realizados:

Monitor de Mão de Obra:

Monitor de Equipamento:

A improdutividade gera custo ao projeto e não agrega valor. O cadastro de improdutividade é importante para registrar apontamentos de períodos improdutivos de insumos e/ou equipamentos, e mensurar o quanto estes ficaram parados por algum impedimento.

**Integrado com SIGAMNT**  
 

Quando o parâmetro “Integrado com o SIGA-MNT” estiver HABILITADO. significa que o TCOP está utilizando a integração com o SIGAMNT do PROTHEUS, com isso, a manutenção dos motivo de improdutividade para **EQUIPAMENTOS** são realizadas através do cadastro de atividades do módulo de manutenção do Protheus.

Os registros sincronizados do SIGAMNT do tipo “Equipamento” não poderão ser alterados no TCOP. Somente os registros de motivo de improdutividade de Mão de obra terão a manutenção no TCOP;

A sincronização é feita via Mensagem Única:

* + **Código:** 1005;
  + **Descrição:** TOTVS Construção Obras e Projetos x Manutenção de Ativos;
  + **Mensagem/Versão:** ACTIVITY / 1.000

---
