---
article_id: 360055864154
category: Gestão de Frotas
content_hash: 00c9b74c57f6cb34bc35e543d869ae0869a74b610be6cc8ccb198a8ef4e9c288
fetched_at: '2026-06-28T22:42:39.305330+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Atualização do contador de bens de uma
  estrutura no abastecimento do pai
type: support-article
updated_at: '2021-08-13T16:49:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055864154-Manufatura-Linha-Protheus-MNT-Atualiza%C3%A7%C3%A3o-do-contador-de-bens-de-uma-estrutura-no-abastecimento-do-pai
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:30 min**  
**Dúvida**Ao lançar **Abastecimento** no **Equipamento** principal da **Estrutura**, o **Contador** dos demais **Equipamentos** também é atualizado, porém, todos os equipamentos contém contador próprio. O Sistema considera a **Estrutura** ou o **Contador** individual de cada um?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12  
  
**Solução**Para que um **Bem** receba **Contador** é necessário que o campo **Tem contador - T9\_TEMCONT** seja igual a **S - Sim**:

1. Se um **Bem** tem **Contador** próprio ele só receberá incremento de **Contador** quando for reportado diretamente à ele;
2. Se um **Bem** for orientado pelo pai da **Estrutura** ou pelo pai imediato ele receberá incremento de **Contador** quando este pai receber um reporte;
3. Se um **Bem** não possuir **Contador** jamais receberá incremento.

**Exemplo**

1. Acessar o módulo **Manutenção de Ativos**.
2. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Produtos**, incluir um produto.
3. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Funcionários**, incluir um funcionário.
4. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Motoristas**, incluir um motorista, informando um número de **CPF - Cadastro de Pessoa Física**.
5. Em **Atualizações - Controle de Oficina - Cadastros Básicos - Fornecedores**, incluir um fornecedor.
6. Em **Atualizações - Controle de Combustíveis - Cadastros Postos - Tipos de Combustíveis**, incluir um combustível.
7. Em **Atualizações - Controle de Combustíveis - Cadastros Postos - Postos**, incluir dois postos bem como a **Negociação** e o **Preço**.
8. Em **Atualizações - Controle de Combustíveis - Cadastros Postos - Posto Interno**, clicar em **Tanques/Bombas**. Informar um tanque e relacioná-lo ao produto incluído anteriormente.
9. Em **Atualizações - Controle de Oficina - Bens - Família de Bens**, incluir duas novas famílias de bens, uma para **Bem** outra para **Pneu**.
10. Em **Atualizações - Controle de Oficina - Bens - Modelos**, incluir dois novos modelos de bens, um para **Bem** outra para **Pneu**.
11. Em **Atualizações - Controle de Oficina - Bens - Bens**, incluir um **Bem** com campo **Categoria** igual a **4 - Frota Não Integrada ao TMS** e campo **Tem Contador** igual a **S - Tem Contador Próprio**. Na aba **Complemento Veículo**, preencher os dados referente aos campos **Placa** e **Tipo Veículo**. Em **Ações Relacionadas**, clicar em **Tanque** e informar um tanque de combustível para o **Bem**, relacionando ao **Tipo de combustível** informado no **passo 6**.
12. Na mesma rotina de **Bens**, incluir os **Pneus**, da categoria **3 - Pneu**, relacionando a família e o modelo do devido pneu e atrelar contador próprio.
13. Em **Atualizações - Controle de Oficina - Bens - Estrutura Padrão**, incluir uma estrutura padrão informando a **Família** e o modelo do **Bem**, selecionar o componente e relacionar as localizações informando a **Família do Pneu**.
14. Em **Atualizações - Controle de Pneus - Estrutura - Esquema Mod. 2**, incluir um esquema padrão, informando a **Família** e modelo do **Bem** e atrelando a estrutura à família e localização do **Pneu**.
15. Em **Atualizações - Controle de Oficina - Manutenção - Serviços** cadastrar serviços com tipo de manutenção **Corretivo** e **Código de serviço** igual aos valores dos parâmetros configurados anteriormente. Exemplos de códigos: **PNEREF**, **PNECON**, **PNEMOV**, etc.
16. Em **Atualizações - Controle de Oficina - Ordem de Serviço - Corretiva**, incluir uma ordem de serviço corretiva com situação **Liberado**, informando o **Bem** e o **Tipo do serviço** cadastrado.
17. Selecionando a **O.S. - Ordem de serviço** incluída, acessar **Outras Ações - Rodados** incluir pneus na estrutura do bem.
18. Em **Atualizações - Controle de Combustíveis - Abastecimento - Abast. Manual**, incluir um abastecimento.
