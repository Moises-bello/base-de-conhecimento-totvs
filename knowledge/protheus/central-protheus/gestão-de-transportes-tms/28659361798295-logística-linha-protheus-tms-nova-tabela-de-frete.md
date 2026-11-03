---
article_id: 28659361798295
category: Gestão de Transportes (TMS)
content_hash: bde078c5c9b5e5cd612e1636770b07fb5a7327fe2821f274f0c3656a49689e48
fetched_at: '2026-06-28T22:45:29.474125+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Nova Tabela de Frete
type: support-article
updated_at: '2024-12-23T18:31:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28659361798295-Log%C3%ADstica-Linha-Protheus-TMS-Nova-Tabela-de-Frete
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28659345778455) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais foram as alterações na funcionalidade Nova Tabela de Frete?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**O objetivo da nova Tabela de Frete se mantem, e as alterações que foram realizadas, serão destacadas no decorrer desta documentação.

O dicionário de dados relacionado à antiga Tabela de Frete foi reorganizado para que fosse possível a elaboração da nova rotina Tabela de Frete.

As tabelas relacionadas a rotina anterior **Tabela de Frete - TMSA010** são:

* **DTL - Configuração da Tab. Frete**;
* **DVE - Itens Config. Tabela de Frete**;
* **DT0 - Tabela de Frete**;
* **DTK - Complemento de Tabela de Frete**;
* **DT1 - Itens de Tabela de Frete**;
* **DW1 - Subitens de Tabela de Frete**;
* **DY1 - Excedente subfaixa tab. frete**;
* **DVY - Base Componente TDA**;
* **DJS - Base Calc % Componente Frete**.

Para a **Nova Tabela de Frete -TMSA010B**, para que essa nova rotina fosse adequada e funcional ao modelo MVC - *Model-View-Controller,* houve a criação da tabela **DNJ - Componentes Tabela de Frete**, em seu índice foram inseridos origem e destino. Esta alteração estrutural permite na nova rotina que existam mais de 99 componentes para o cadastro da tabela frete. Desta forma, o uso da tabela **DNJ** requer que os componentes sejam relacionados à origem e destino.  
Na rotina anterior de Tabela de Frete existia uma limitação de cadastro de componentes, e com o uso da Nova Tabela de Frete não há essa limitação.   
O cadastro com possibilidade de inclusão de origem e destino por componente exponencia a quantidade de registros na DNJ.  
  
**Compatibilização**  
Para que Tabelas de Frete criadas na rotina antiga Tabela de Frete possam ser visualizadas e alteradas para a nova rotina Nova Tabela de Frete, foi disponibilizada no botão **Outras Ações** > **Compatibiliza Tabelas**.

![compatibiliza .png](https://centraldeatendimento.totvs.com/hc/article_attachments/28661851938967)

Ao utilizar esta opção o sistema ajusta/cria a tabela **DNJ - Componentes Tabela de Frete**, para tabelas pré-existentes.  
  
**EXEMPLO DE UTILIZAÇÃO**  
Para cadastrar a Tabela de Frete: No **SIGATMS**, clique em **Atualizações** > **Comercial** > **Nova Tabela de Frete** > **Incluir**.  
Na sequência é apresentada a tela que permite selecionar a configuração da Tabela de Frete.

![config.tabela.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28661851941527)

Os itens apresentados nesta tela foram configurados anteriormente na rotina **Configuração da Tabela de Frete - TMSA130**. Selecione a configuração da Tabela de Frete clicando sobre o item desejado e confirme.  
Em seguida, é apresentada a tela Tabela de Frete - Incluir. Informe os campos:  
**Código da Região Origem e Código da Região Destino:** são utilizados para o cálculo do frete, indicando os trechos de possíveis viagens e seus respectivos valores de frete. É obrigatório que esta região seja previamente definida como região de origem ou destino no cadastro **Complemento de Região - TMSA380**.  
**Código da Tabela de Tarifa:** permite vincular uma Tabela de Tarifas à Tabela de Frete. Assim, os valores dos componentes de frete serão preenchidos automaticamente.  
**Produto:** utilizado para cadastrar uma tabela específica para este produto. Caso não seja informado, indica que os valores desta tabela são aplicados para todos os produtos.  
Na sessão **Componentes de Frete**, serão listados os componentes assim que forem digitadas as informação de Origem e Destino:

![componente.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28661837447191)

Diferente da rotina anterior Tabela de Frete, para realizar a configuração definindo: as faixas, valores ou intervalos para o cálculo do frete de cada componente, será necessário posicionar primeiro no componente a ser configurado e na sequencia selecionar a aba Faixa, Subfaixa (caso o componente seja definido como subfaixa e seguido as regras pré-existentes) e Outros.  
Devem ser observado o preenchimento dos campos: **Até**, **Fator Peso**, **Valor, Fração** e **Componente Tarifa**. Na seção Complemento Tabela de Frete e Complemento de Subfaixa, informe os dados complementares a Tabela de Frete (Mínimo de Excesso e Valor Mínimo).  
Para cada componente é possível configurar:

* **Mínimo de Excesso**: informação utilizada para o cálculo do frete;
* **Valor Mínimo:** valor a ser cobrado por componente pelo serviço realizado;

Confira os dados e confirme.

**Observação:** Os componentes apresentados com asterisco representam as tarifas pertencentes a região superior da estrutura de regiões.  
  
**Importante**  
Para utilização da nova funcionalidade, deve-se rodar o **UPDDISTRI** do pacote **012766** (em anexo) para atualização de dicionário de dados, criação de novas tabelas **DNJ** e **DNL**, campos, índices, gatilhos.  
  
**Saiba mais**  
Verifique mais detalhes nas documentações [Nova Tabela de Frete (TMSA010B - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=809134095) e [DT DLOGTMS02-23852 Nova Tabela de Frete.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=809132686)   
Para mais informações de como realizar o procedimento do **UPDDISTRI** verifique a documentação [Upgrade de Release do Protheus 12](https://tdn.totvs.com/pages/releaseview.action?pageId=181965468)
