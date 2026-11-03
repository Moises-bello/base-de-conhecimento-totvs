---
article_id: 360020186252
category: Rescisão
content_hash: 67da663c59af79724891ee34853e8c01db79f3484f88d189e2c92048949a52f6
fetched_at: '2026-06-28T22:46:55.361850+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Transferência entre filiais ou coligadas
type: support-article
updated_at: '2024-06-17T15:11:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020186252-RH-RM-FOP-Transfer%C3%AAncia-entre-filiais-ou-coligadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24231616268183) Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Como realizar a transferência de um funcionário entre filiais ou coligadas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a transferência de um funcionário entre filiais ou coligadas, siga os passos abaixo:  
  
1. Acesse: **Administração de Pessoal | Funcionários | selecione a chapa do funcionário | ícone** **Rescisão**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907334492823)  
  
2. Na aba **Aviso Prévio** | campo **tipo de demissão**, informe os tipos **5 - Transferência sem ônus p/ Cedente** ou **6 - Transferência com ônus p/ Cedente.**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907337227671)  
  
3. Na aba **Rescisão,** preencha as informações como a data de demissão, o motivo da mudança e o motivo da demissão, salve a rescisão e transfira o funcionário clicando no botão **Transferir Funcionário.**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907376692119)  
  
4. Insira os parâmetros para a transferência, verificando se a transferência se dará para a mesma filial ou coligada e os históricos que deverão ser transferidos.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907452092055)

* **Alterar Chapa do Funcionário Demitido:** Se altera a chapa do funcionário demitido mantem o número da chapa antiga para o novo registro do funcionário ativo, apenas deve ser verificado que a transferência para o próximo mês altera a chapa do funcionário que ficará A – ativo e o chapa antiga ficará com o funcionário tipo D- demitido. Portanto, isso significa que se você marcar este parâmetro, o funcionário demitido passará a ter a chapa que você informa no momento da transferência, mantendo a chapa original no funcionário que ficará ativo.
* **Realiza transferência para outra base de dados:** Marcando este parâmetro o funcionário é demitido por transferência, porém o sistema não faz nenhum outro tratamento interno, e apresenta uma alerta de que este funcionário não será mais tratado pelo RM Labore. Marcando este parâmetro o sistema desabilita os campos **Nova Coligada** e **Realiza transferência para mesma coligada.**
* **Transfere Históricos​:**Se transfere históricos, opção que somente será apresentada caso não haja transferência para mesma coligada. Serão copiados os históricos de Férias, incluindo os recibos, função, salário, afastamento, contribuição sindical, horário, provisão. Para estes históricos deve haver compatibilidade dos códigos entre as coligadas, sob a responsabilidade do usuário. Serão feitas algumas verificações de inconsistências e caso ocorram a transferência será cancelada. Vale lembrar que, o Histórico de Seção não será copiado em caso de transferência entre coligadas. Isto é devido pelo fato de ocorrer incompatibilidade de códigos, descrições e demais dados das seções entre a coligada cedente e a coligada destino.
* **Transfere Históricos de Provisões:**Quando marcada a flag para enviar o histórico, ele mantém o histórico na coligada de origem, para fins de relatórios futuros, se necessário, e leva todo o histórico para a coligada destino.
* **Transfere históricos de encargos:** Poderá transferir todos ou apenas os selecionados, selecione o que deseja transferir.
* **Transfere apenas da competência anterior:** Com este parâmetro marcado o sistema irá transferir apenas os históricos da competência anterior. Então, caso deseje transferir todos os meses não deve marcar este parâmetro.
* **Transfere rateio por centro de custo:** Marque esta opção caso deseje transferir juntamente com o histórico do encargo a opção de **Rateio de Encargo por centro de custo.**
* **Motivo da Transferência:**

**-->**Quando a Transferência é do tipo **5- Transferência sem ônus p/ Cedente** e mesma coligada ou o usuário desmarca o parâmetro **Realiza Transferência para mesma coligada** e informa a nova coligada com o CNPJ com a mesma raiz da coligada de origem, o processo desabilita as opções de Motivo da Transferência para o usuário selecionar e por default deixa o Motivo da Transferência **Estabelecimentos da própria empresa** selecionado. Com este motivo de Transferência, o processo não irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial.  
  
**-->** Quando a Transferência é do tipo **6- Transferência com ônus p/ Cedente**, as opções de Motivo da Transferência ficam desabilitadas para o usuário selecionar. Com este tipo de transferência o processo irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial, conforme a Máscara para Matrícula do Trabalhador configurada em **Configurações | Parâmetros | Parametrizador | 06.07- eSocial | Configurações Gerais.**  
  
**-->**Quando a Transferência é do tipo 5- Transferência sem ônus p/ Cedente e o usuário desmarca o parâmetro **Realiza Transferência para mesma coligada**  e informa a nova coligada com o CNPJ com raiz diferente da coligada de origem, o processo habilita as opções de Motivo da Transferência para o usuário selecionar, podendo ser **Sucessão, incorporação, cisão ou fusão** ou **Empresa do mesmo Grupo Econômico.** O Motivo da Transferência **Estabelecimentos da própria empresa** fica desabilitado para ser selecionado. Com estes motivos de Transferência, o processo irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial, conforme a Máscara para Matrícula do Trabalhador configurada em **Configurações | Parâmetros | Parametrizador | 06.07- eSocial | Configurações Gerais.**

* **Transfere Movimentação do mês atual:** Durante o processo de transferência marcando o parâmetro: **Transfere movimentação do mês atua**l, o sistema apaga os registros da chapa do funcionário demitido e leva esta movimentação para a chapa ativa. Segue print demonstrando:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907459266327)  
  
5. Informe os dados da transferência: **nova seção, nova função, novo horário, novo salário e a conta bancária.**  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907479282455)  
  
6. Avance e execute o processo da rescisão. Após a transferência do funcionário ele ficará com situação **D- Demitido** na chapa antiga, não sendo possível mais realizar movimentações.  
  
**Importante**  
A transferência do funcionário é **irreversível** e não pode ser cancelada! Antes de executar o processo, tenha certeza das informações digitadas no cadastro da rescisão.  
  
No tipo de rescisão **5 - Transferência sem ônus p/ Cedente,** a empresa que está cedendo o funcionário não terá custo com a rescisão. Ou seja, a filial ou a outra empresa destino irá arcar com o passivo trabalhista.  
  
No tipo de rescisão **6 - Transferência com ônus p/ Cedente,** a empresa cedente irá realizar a rescisão arcando com todo o passivo trabalhista do funcionário.
