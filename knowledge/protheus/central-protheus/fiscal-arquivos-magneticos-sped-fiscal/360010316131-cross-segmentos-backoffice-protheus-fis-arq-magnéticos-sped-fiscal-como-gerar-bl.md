---
article_id: 360010316131
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 76d612d7e78805af6693645f4acc2860433666a68f34641795a8e92e7aa0aa59
fetched_at: '2026-06-28T22:42:02.490528+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  – Como gerar bloco H - Inventário Físico e Controle de Estoque
type: support-article
updated_at: '2024-06-13T17:55:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316131-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-bloco-H-Invent%C3%A1rio-F%C3%ADsico-e-Controle-de-Estoque
---

# 

**Dúvida**

Inventário Físico e Controle de Estoque

**Ambiente**

Protheus à partir da versão 12.1.23

**Solução**

 Em virtude da instabilidade da versão atual do programa de extração do bloco H, tomamos a decisão de voltar ao método antigo de processamento, apoiado no arquivo de trabalho gerado pelo relatório de**Registro de Inventário Mod. P7 (MATR460**). Este método será mantido até a completa estabilização da versão atual do programa extrator.  
  
Desta forma, será necessária a emissão do relatório **MATR460** (configurado em seus parâmetros para gerar o arquivo) antes da execução da rotina **SPEDFISCAL**. Não haverá parametrização no programa **SPEDFISCAL** quanto a leitura do arquivo gerado pelo **MATR460** pois este lerá os parâmetros do relatório para obtenção do arquivo.

Os registros contidos neste bloco não são de apresentação obrigatória. Por isso foi disponibilizado no w*izard* da rotina uma pergunta, deixando a critério do usuário a geração ou não dessas informações. Os registros somente são gerados se a pergunta **Gera Inventário** estiver preenchida como **Sim** e o **Data de fechamento do estoque**  igual data de fechamento emitido no relatório **MATR460**.

# Importante

Todas as informações do **Bloco H** são geradas por meio do arquivo gerado pelo **Reg. Invent. Mod. 7** **(MATR460)** criado na pasta *System*, este arquivo é um espelho do relatório com saldo em estoque, saldo de terceiros, saldo em terceiros e saldo em processo.

# Pacotes de Correção/Atualização (Bloco H e K)

Atenção: Para geração dos blocos H e K e essencial a atualização dos fontes MATR460, MATXSPED e SPEDXFUN através da patch de programas abaixo:

BLOCO H e K - Pacotes Essenciais para geração dos blocos

**Pacote de Atualização 1**

**MATR460:**

**12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=697755> ;**

**12.1.16: <https://suporte.totvs.com/portal/p/10098/download?e=697757> ;**

**Pacote de Atualização 2 - MATXSPED e SPEDFISCAL:**

**12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=691157> ;**

**12.1.16: <https://suporte.totvs.com/portal/p/10098/download?e=691156> ;**

**Aplique os pacotes 1 e 2 com a opção "Atualizar somente fontes atualizados" marcada.**

![(aviso)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/warning.png) Atenção: Aviso da Receita sobre problemas no validador (PVA) para o Bloco K

<http://sped.rfb.gov.br/pagina/show/2522>

![](http://tdn.totvs.com/download/attachments/271656762/image2018-2-8_9-20-41.png?version=1&modificationDate=1518088841000&api=v2)

**Registro tipo H001 - Abertura do bloco H**

Contém a identificação do registro e um campo informando se há movimentos para este bloco.

**Registro tipo H005 - Totais do inventário**

Este registro contém os totais do inventário.

**Registro tipo H010 - Inventário**

Este registro apresenta um resumo do inventário disponível, informações são obtidas do arquivo gerado pelo relatório **Reg. Invent. Mod. 7 (MATR460). Segue processo e validação para geração do registro:**

No momento da geração do Relatório **Reg. Invent. Mod. 7 (MATR460)**, configurar as perguntas da seguinte maneira:

* + **Gerar Exp. SPED FISCAL** =  SIM // Para gerar DBF na Pasta System, para ser levado para SPED FISCAL no Bloco H.
  + **Data de fechamento de estoque** = 31/12/2017//Data do arquivo de Inventario, de quando foi fechado.
  + **Arquivo Exp. Spedfiscal**= 20171231 //Informe o nome do arquivo com mesma data a ser informado na **Data de fechamento do estoque** - Informe a data em que foi feito o fechamento do estoque, caso queira gerar os registros de inventário.

# IMPORTANTE :

# Os campos abaixo, devem possuir o mesmos dados ou seja o nome do arquivo " Arquivo Exp. Spedfiscal "vai ser a data de fechamento de estoque, no campo Arquivo Exp. Sped Fiscal, o formato é (AAAAMMDD).

Exemplo:

![](http://tdn.totvs.com/download/attachments/271656762/image2018-3-1_14-25-58.png?version=1&modificationDate=1519925160000&api=v2)

*Importante - Para quando se tratar de FILIAL:*

***Arquivo gravado na pasta :***

*![](http://tdn.totvs.com/download/attachments/271656762/image2017-4-27%2014%3A31%3A42.png?version=1&modificationDate=1520613434000&api=v2)*

***Formação do Arquivo 20170427d\_MG\_01 :***

*20170427 (Data informada na impressão do relatório)*

*D\_MG\_01 Filial utilizada, sendo (D) Empresa (MG) Unidade (01) filial*

*OBS: A informação de filial é gerada automaticamente pelo sistema permitindo deixar vários períodos armazenados no diretório que o arquivo do relatório foi gerado.*

***Esse tratamento permite que sejam gerados vários períodos para serem processados pelo SPEDFISCAL***

*Depois de gerado o relatório o arquivo estará na pasta System com o nome informando no relatório. (O arquivo não deve ser apagado.)*

IMPORTANTE - Mudanças na tratativa do Arquivo Temporário

A partir da release 12.1.017 utilizando os fontes MATR460.PRW (Registro de inventario Mod. P7) e MATXSPED.PRW (Biblioteca responsável pela geração dos registros do bloco K) com data igual ou superior a 14/06/2018, os arquivos temporários não serão mais disponibilizados na pasta System, porém, o processo para geração do bloco H se mantêm. As informações geradas irão estar disponíveis somente para a geração do arquivo magnético SPEDFISCAL.

Os novos arquivos serão gerados utilizando o novo driver SQLLITE (interno do produto), caso tenha customizações no arquivo de temporário de integração (Entre o relatório Registro de Inventario P7 e SpedFiscal) recomendo que utilize nossos pontos de entrada.

Para maiores informações sobre o SQLLite consulte link: <http://tdn.totvs.com/display/tec/DBSqlExec>

E no momento da geração do arquivo magnético **SPEDFISCAL**, o fonte está realizando seguinte validação nas perguntas de **WIZARD**:

* + **Gera Inventário** = Sim// Selecione se deseja gerar os registros de inventário (bloco H).
  + **Data de fechamento do estoque**= Informe a data em que foi feito o fechamento do estoque, caso queira gerar os registros de inventário. Onde fonte irá buscar na sua pasta /SYSTEM/ .DBF ou .DTC com a mesma data gerado pelo Relatório Reg. Invent. Mod. 7 (MATR460).
  + **Motivo do Inventário -**Selecione qual o motivo do inventário:

              01 – No final no período;

# Importante

A partir do período de Janeiro de 2015, será gerado o novo campo 11-VL\_ITEM\_IR no registro H010. Este novo campo será  gerado baseando-se no valor de custo médio, que é o tipo de custo processado pelo sistema .

Incluído ponto de entrada **SPEDALTH** para processamento do registro H010 SPED FISCAL.

<http://tdn.totvs.com/x/l6Q4E>

Ponto de entrada para alteração conta contábil:

[SPDFIS07 - Conta Contábil registro H010](http://tdn.totvs.com/pages/viewpage.action?pageId=270085353)

Segue vídeo evidenciando o processo de geração do Registro H010 do Arquivo magnético SPEDFISCAL:

[![](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/2.0.4/_/download/resources/com.atlassian.confluence.plugins.confluence-view-file-macro:view-file-macro-resources/images/placeholder-medium-zip.png)](http://tdn.totvs.com/download/attachments/271656762/P12.1.17_SPEDFISCAL_H010_FDL.avi.zip?version=1&modificationDate=1517915233000&api=v2)

[P12.1.17\_SPEDFISCAL\_H010\_FDL.avi.zip](http://tdn.totvs.com/download/attachments/271656762/P12.1.17_SPEDFISCAL_H010_FDL.avi.zip?version=1&modificationDate=1517915233000&api=v2)

**Registro tipo H020 - Informação complementar do Inventário**

**Para geração deste registro, já existe uma FAQ com o processo e validação:**

**[ARQ0013\_H020\_SPED\_FISCAL](http://tdn.totvs.com/display/PROT/ARQ0013_H020_SPED_FISCAL)**

Preencha o conteúdo deste registro para complementar as informações do inventário, quando o campo MOT\_INV do registro H005 for de **02** a **05**. Onde essas informação é obtida na WIZARD do **SPEDFISCAL:**

* + **Motivo do Inventário -**Selecione qual o motivo do inventário:

          02 – Na mudança de forma de tributação da mercadoria (ICMS);

          03 – Na solicitação da baixa cadastral, paralisação temporária e outras situações;

          04 – Na alteração de regime de pagamento – Condição do contribuinte;

          05 – Por determinação dos fiscos.

# Importante

Caso selecione a opção por 02 (mudança da forma de tributação da mercadoria de ICMS) somente são gerados os registros para os produtos que sofram alteração da tributação de ICMS. Para identificação desses produtos está disponível o campo na tabela SB5 **(B5\_ALTTRIB)** para informar se houve ou não alteração da tributação do ICMS.

Os produtos com quantidade zerada são gerados no SPEDFISCAL e também se forem listados no relatório de inventário P7.

**Registro tipo H990 - Encerramento do bloco H**

Contém a identificação do registro e um campo informando a quantidade de registros do bloco **H**.

Para mais informações sobre o Sped Fiscal, acessar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
