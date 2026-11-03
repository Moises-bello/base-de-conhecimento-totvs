---
content_hash: 97a57993c30fdd8de916743ddad9374c38f7e4162e7b7389dec3d5af08bbe7dc
fetched_at: '2026-06-29T00:09:53.777490+00:00'
page_id: '441821303'
product: rm
source: tdn-rm
title: Integração RM x Carol - Importação de Batidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=441821303
version: 22
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Automação de Ponto |
| **Versões:** | 12.1.29 |
| **Passo a passo:** | Neste documento iremos demonstrar as mudanças feitas no processo de importação de batidas:  **Importante:** A integração RM x Carol atende a Portaria 671, o funcionário agora é reconhecido pelo CPF.  **RM.exe**  A configuração básica para utilização da importação de batidas através da Carol, consiste em informar no parametrizador, que o sistema irá utilizar a integração.  Para isso, basta acessar o menu **Configurações | Parametrizador**, no processo 08.01 - Iniciais, avance até a Etapa 5 - Integração-Integração Carol/TSA.    Ao Selecionar o parâmetro **"Considera integração com as batidas da Carol",**  será visualizado o quadro **"Parametrização Ambiente Carol".**  Para utilizar a Integração com a Carol, é necessário preencher os campos: Nome da organização, Nome do ambiente, Usuário e Senha.  **Importante:**  O "Nome da organização " virá em branco , devendo ser preenchido pelo usuário conforme sua organização.  O usuário terá a opção de [Importar batidas fora do Perímetro](https://tdn.totvs.com/pages/releaseview.action?pageId=452718976).      Para realizar a importação de batidas acesse o menu **Entrada de Dados | Importar.** Na tela de importação, ao configurar o parametrizador da forma demonstrada acima, irá habilitar o parâmetro **"Utiliza integração com a Carol".**      Ao marcar este parâmetro, as seguintes opções serão desabilitadas:   * Arquivo para importação; * Layout do Relógio; * Grupo de Funcionários; * Terminal de Coleta para Histórico; * Considera natureza fixa;   A  opção   "Considera o último NSR importado " ficará habilitada e permitirá ao usuário definir se a importação será por Período ou NSR.  Com o parâmetro desmarcado, será realizada a importação por Período      Com o  parâmetro marcado, a importação irá considerar o Ùltimo NRS gerado pela Carol e não será permitida a importação por período.  A opção Período de importação ficará desabilitada .    Ao executar o processo, as batidas serão recuperadas através da plataforma Carol. Dentro do período de importação definido, o processo busca todos os dispositivos ativos cadastrados (que realizam integração com o RM) e realiza a importação de acordo com a última batida importada de cada dispositivo. Dessa forma, são criados registros de importação para todos os dispositivos cadastrados na tabela AHSTIMPORTACAO.    Após realizar a importação, no menu **Entrada de Dados | Layout** é criado automaticamente um registro de layout de relógio para identificar importações provenientes da Carol.      **OBSERVAÇÃO:** Enquanto a barra de progresso do processo estiver em 0% significa que as batidas estão sendo recuperadas da plataforma Carol e por isso, o processo pode se manter neste status por alguns minutos.  **IMPORTANTE:**  Caso o usuário exclua ou altere o horário de alguma batida a mesma não será reimportada pela Carol, o ajuste deverá ser realizado manualmente.  Batidas canceladas serão reimportadas.  **AVISO:** Essa funcionalidade foi criada pela TOTVS LABS, qualquer dúvida em relação a esta funcionalidade deverá entrar em contato com o atendimento da Carol [suporte.carol@totvs.com.br](mailto:suporte.carol@totvs.com.br). |
