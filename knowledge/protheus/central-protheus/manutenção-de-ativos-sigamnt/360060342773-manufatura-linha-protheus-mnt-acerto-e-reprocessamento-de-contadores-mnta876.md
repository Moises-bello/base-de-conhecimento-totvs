---
article_id: 360060342773
category: Manutenção de Ativos (SIGAMNT)
content_hash: 8f0f926d11e8884b5d0f9e5ca55f4ce5f7a9943068c74609347d993f45b14c2a
fetched_at: '2026-06-28T22:42:32.684646+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Acerto e Reprocessamento de Contadores
  - MNTA876
type: support-article
updated_at: '2024-09-13T19:32:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060342773-Manufatura-Linha-Protheus-MNT-Acerto-e-Reprocessamento-de-Contadores-MNTA876
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26359213407767) Tempo aproximado para leitura: **00:08:00 min**  
**Dúvida**Como são realizados o **Acerto e Reprocessamento de Contadores - MNTA876**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O reprocessamento de contador utilizado na rotina **Acerto e Reprocessamento de Contadores - MNTA876** é destinado a bens de qualquer categoria, controlados por **contador próprio**, desta forma cadastrados informando o campo **T9\_TEMCONT -** **Tem Contador = S**.Este reprocessamento é exclusivo para o histórico do **primeiro contador**do bem, não sendo possível reprocessar os registros de segundo contador.  
Para a efetividade do reprocessamento é necessário se realizar a exportação do arquivo de histórico e posteriormente sua importação como descritos abaixo.  
  
**Exportação**:  
Ao selecionar a opção de **exportação** o usuário poderá identificar todos os seus bens cadastrados em uma listagem no formato de *markbrowse*, onde é possível selecionar diversos bens para a geração do arquivo de importação.  
Confirmando a seleção dos bens, o Sistema irá gerar um arquivo com extensão **.dbf** ou **.dtc** conforme o ambiente do cliente, com os campos **TP\_FILIAL -** **Filial**, **TP\_CODBEM - Bem**, **TP\_DTLEITU -** **Data Leitura** , **TP\_HORA -** **Hora**, **TP\_POSCONT -** **Contador**, **TP\_ ACUMCON -** **Ac. Contador** e **TP\_TIPOLAN -** **Tipo Lancam**, em pasta específica dentro do dicionário do ambiente, no caminho **ROOTPATH + STARTPATH + \ NG.** Exemplo: **Protheus\_Data\ System\_XXXXX\ NG**.  
  
Para essa opção devem ser observado:

* Quanto maior o número de bens selecionados maior será o tempo de processamento e mais complexo poderá ser o trabalho de ajustes manuais no arquivo ao importar.
* É importante ressaltar que o campo de variação dia não é exportado visto que seu valor é consequência do reporte de contador, assim não deve ser informado manualmente. Seu cálculo  baseia-se na fórmula:  
  **Variação Dia = (Contador Acumulado Final – Contador Acumulado Inicial) / Diferença de Dias entre reportes)**.
* Também é possível realizar **exportação parcial do histórico**. Para isso, junto a seleção da opção **Exportar Histórico de Contador**, marque também a funcionalidade **Exportação Parcial** e informe a data desejada no campo **A partir de**. Esta funcionalidade visa apoiar usuários que desejam realizar ajustes pontuais no histórico, sem a necessidade de reprocessar todo o histórico de contador dos bens selecionados.

**Importação**:  
Através da própria rotina é possível selecionar também a opção **Importar Histórico**. Nesta opção, o usuário tem a possibilidade de incluir novos registros como também alterar ou excluir os registros existentes no histórico, através de uma interface em *getdados*, que é apresentada logo após a seleção do arquivo gerado na exportação.   
Para esta manutenção do arquivo há algumas regras que devem ser observadas como:

* O primeiro registro do arquivo deve ser do tipo de lançamento **I - Inclusão**, com exceção dos arquivos provenientes de exportação parcial;
* Só é possível alterar contador acumulado caso o registro seja do tipo **I - Inclusão**, haja visto que o Sistema no momento do reprocessamento irá realizar o recálculo do contador acumulado correspondente a aquele registro com base nos reportes de posição desde a inclusão do bem;
* A inclusão de novos registros é permitida, porém somente serão consistidos registros do tipo **I - Inclusão, C - Contador, Q - Quebra ou V - Virada**. Registros do tipo **A - Abastecimento**, devem ter um abastecimento relacionado, caso contrário irá cair na validação de consistência;
* A posição de contador não pode ficar em branco ou zerada, assim como o campo de filial caso a tabela **STP** **- Histórico de apontamento do 1º Contador** não esteja em modo compartilhado.

Ao finalizar a edição deste arquivo e confirmar no botão **OK**, é realizada a leitura dos registros alterados em tela, gravando-os em uma tabela temporária, no mesmo formato do arquivo exportado, de forma ordenada por **Código do bem** mais **data** e hora de leitura mais **filial**. Além disso, é criado um *backup* da tabela **STP** referente aos bens selecionados, no diretório **Protheus** em **ROOTPATH + STARTPATH + \NG + \backup**, no formato **STPXX0\_YYYYMMDDHHMMSS\_backup.dtc**, sendo **YYYYMMDD** e **HHMMSS** substituídos pela data e hora do processamento.  
É importante se atentar que este *backup* será excluído ao final do processamento quando o mesmo for efetivado com sucesso.  
Para apoiar o usuário neste reprocessamento, todos os registros serão validados pelo Sistema, de forma a consistir a integridade do histórico de contador com as tabelas relacionadas que utilizam a informação, sendo as principais:**ST9 - Bens, STJ - Ordens de Serviço, STZ - Movimentação de Bens, TQN - Abastecimentos, TQ2 - Transferência de Bens, TQB - Solicitação de Serviço, TPN - Utilização de Bens, TTI - Entrada/Saída de Veículos e STF - Manutenção**. O reprocessamento só será completado com sucesso quando todas as inconsistências forem verificadas e corrigidas.  
  
**Importante**Segue o procedimento para utilização da rotina:

1. No módulo de **Manutenção de Ativos** acesse **Atualizações / Controle de Oficina / Contador / Acerto - MNTA875.**
2. O Sistema apresenta uma nova janela com as opções: **Acerto Individual de Contador, Ajuste/Reprocessamento de Contador Próprio e Reprocessamento de Contador em Estrutura (Componentes).**
3. Escolha a opção de **Ajuste/Reprocessamento de Contador Próprio** e clique em **Confirmar**.
4. Logo após, uma nova janela com duas opções é apresentada.
5. Selecione a opção **Exportar histórico de Contador.**
6. O Sistema irá apresentar uma nova janela, onde é **possível visualizar todos os bens disponíveis na empresa, controlados por contador próprio.**
7. **Selecione os bens que pretende realizar o ajuste de contador** e clique em **OK**.
8. Logo após o Sistema apresenta uma nova janela, onde é possível agora visualizar o **nome do arquivo** e se desejar este pode ser alterado. Clique em **OK** para prosseguir.
9. O Sistema cria um arquivo com todo o **histórico de contador dos bens selecionados**, no **diretório do ambiente do dicionário Protheus dentro de pasta NG** com extensão em **.dtc** ou **.dbf**, conforme ambiente do cliente.
10. Novamente em **Atualizações / Controle de Oficina / Contador / Acerto - MNTA875**, escolha a opção de **Ajuste/Reprocessamento de Contador Próprio - MNTA876** e prossiga.
11. Selecione a opção **Importar histórico de Contador** e clique em **Próximo**.
12. O Sistema irá apresentar janela com o diretório do ambiente. **Selecione o arquivo anteriormente criado.**
13. Após a confirmação o Sistema apresenta os registros de contador contidos no arquivo exportado, desta forma **confira os registros presentes no arquivo**, altere ou inclua registros e após a manutenção do arquivo clique em **OK**.
14. O Sistema irá validar todos os registro de acordo com a parametrização informada em **Parâmetros**, botão presente na tela de manutenção dos registros. A validação ocorre também em cima dos demais registros em tabelas relacionadas em todo o ambiente.
15. No final, caso não encontre nenhuma inconsistência nos registros presentes no arquivo, o Sistema irá apresentar a mensagem de **importação realizada com sucesso**. Caso algum erro seja encontrado **será apresentado um log com as inconsistências encontradas**, este visa apoiar o usuário no ajuste de contador, assim como o destaque apresentado em linhas amarelas.
16. Ao corrigir, caso necessário, confirme para que o reprocessamento seja realizado novamente.
17. Ao final do ajuste será apresentado mensagem de **importação realizada com sucesso**, caso ainda os bens ajustados **possuam estrutura de bens**, será apresentado indicação ao usuário que **realize o reprocessamento de contador para bens filhos da estrutura**.
