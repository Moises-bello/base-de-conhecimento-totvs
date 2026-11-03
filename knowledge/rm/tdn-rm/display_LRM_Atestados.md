---
content_hash: 0a28fe2123d8f12a046b84bf5ea46ebb127a5dc04781228497a672cdfc439b0b
fetched_at: '2026-06-29T00:10:05.417588+00:00'
page_id: '452719289'
product: rm
source: tdn-rm
title: Atestados
type: documentation
url: https://tdn.totvs.com/display/LRM/Atestados
version: 8
---

**Atestados**

---

Por  este anexo são cadastrados os atestados médicos entregues pelos funcionários, permitindo, caso desejado, integrar com os módulos de Folha de Pagamento e Automação de Ponto, gerando automaticamente os abonos e afastamentos conforme o tipo de atestado inserido.

Importante: Os atestados estão ligados diretamente à pessoa, no âmbito da coligada corrente, portanto, dentro da mesma coligada é possível visualizar o atestado independente da chapa, porém, sua aplicabilidade (abonos ou afastamentos) estão ligados ao funcionário selecionado no momento da inclusão.

Integração Folha de Pagamento Para atestados que geram afastamentos o sistema obriga o preenchimento do campo "Motivo Afastamento".  
   
Regras aplicadas a atestados que estão associados a afastamentos  
   
1 - Datas de Início e Fim do Atestado em competência anterior a atual competência do Labore:  
      - Sistema não altera a situação do Funcionário  
      - Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do atestado.  
   
2 - Data de Início do Atestado em competência anterior e Fim na atual competência do Labore:  
      - Sistema apresenta uma mensagem ao usuário com opções (exemplo):  
                        *O funcionário está passando da situação "Ativo" para "Af.Previdência"!*  
*Deseja manter o funcionário na situação anterior ao lançamento desse atestado?*  
*- SIM: O funcionário ficará com a situação "Ativo".*  
*- NÃO: O funcionário ficará com a situação "Af.Previdência".*  
   
            Escolhendo a opção SIM:

            - Sistema não altera a situação do Funcionário

            - Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do Atestado.

            Escolhendo a opção NÃO:

            - Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
            - Histórico de Situação é preenchido apenas com a Data Início do Atestado.  
            - Histórico de Afastamento é preenchido com as Datas de Início e Fim.  
  
3 - Data de Início do Atestado em competência anterior e Fim em competência futura:  
            - Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
            - Histórico de Situação é preenchido apenas com a Data Início do Atestado.  
            - Histórico de Afastamento é preenchido com as Datas de Início e Fim.  
  
4 - Data de Início do Atestado em competência anterior e Data Fim não informada:  
            - Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
            - Históricos de Afastamento e Situação são preenchidos apenas com a Data Início do Atestado.  
  
5 - Datas de Início e Fim do Atestado na atual competência do Labore:  
            - Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.  
  
6 - Data de Início do Atestado na atual competência do Labore e Fim em competência futura:  
            - Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.  
  
7 - Data de Início do Atestado na atual competência do Labore e Data Fim não informada:

* Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
              - Históricos de Afastamento e Situação são preenchidos apenas com a Data Início do Atestado.  
    
  8 - Datas de Início e Fim do Atestado em competência futura:  
              - Sistema não altera a situação do Funcionário  
              - Históricos de Afastamento e Situação são preenchidos com as Datas de Início e Fim do Atestado.  
    
  9 - Data de Início em competência futura e Data Fim não informada:  
              - Sistema não altera a situação do Funcionário  
              - Histórico de Afastamento é preenchido com as Datas de Início do Atestado.  
              - Histórico de Situação não é alimentado.

**Foram criadas novas situações para quando uma mensagem perguntando para trocar a situação do Funcionário aparece quando a data fim é inserida em um Atestado que não a possuía.**

1 - Datas de Início e Fim do Atestado em competência anterior à atual competência do Labore:

            - Sistema altera a situação do Funcionário  
            - Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do atestado.  
   
2 - Data de Início do Atestado em competência anterior e Fim na atual competência do Labore:  
            - Sistema apresenta uma mensagem ao usuário com opções (exemplo):

*O funcionário está passando da situação "Af.Previdência" para "Ativo"!*  
*Deseja manter o funcionário na situação anterior ao lançamento desse atestado?*  
*- SIM: O funcionário ficará com a situação "Ativo".*  
*- NÃO: O funcionário ficará com a situação "Af.Previdência".*  
   
         Escolhendo a opção SIM:

        - Sistema não altera a situação do Funcionário  
        - Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do Atestado.

 Escolhendo a opção NÃO:

 - Sistema altera a situação do Funcionário para a Situação Ativo.  
 - Histórico de Situação é preenchido apenas com a Data Início.  
 - Histórico de Afastamento é preenchido com as Datas de Início e Fim.  
   
3 - Data de Início do Atestado em competência anterior e Fim em competência futura:  
 - Sistema não altera a situação do Funcionário  
 - Histórico de Situação é preenchido apenas com a Data Início do Atestado.  
 - Histórico de Afastamento é preenchido com as Datas de Início e Fim.  
    
4 - Datas de Início e Fim do Atestado na atual competência do Labore:  
 - Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.  
              
5  - Data de Início do Atestado na atual competência do Labore e Fim em competência futura:  
    - Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.

 6 - Datas de Início e Fim do Atestado em competência futura:  
    - Sistema não altera a situação do Funcionário  
    - Históricos de Afastamento e Situação são preenchidos com as Datas de Início e Fim do Atestado.  
  
   
Integração Automação de Ponto:

Para atestados que geram abonos o sistema não obriga o preenchimento do campo "Motivo Afastamento". No Automação de Ponto é necessário um recálculo do espelho de ponto do funcionário para que o abono seja considerado e visualizado no anexo "Abono do Funcionário". Neste anexo a origem do abono será: Atestado cadastrado pelo aplicativo RM Vitae.

**Observação**: - Possibilidade de inserir atestados com data anterior e/ou posterior a competência do Folha de Pagamento e período do Automação de Ponto. - Foi adicionado um lookup para informação do profissional de saúde (Código do Médico). Relatório FAP

**Observação**: Ao inserir um atestado para um funcionário deve-se informar se o mesmo é devido à doença ocupacional ou não. Essa informação é necessária ao cálculo da FAP (Fator Acidentário de Prevenção).

**Atenção**: É possível a geração de gráfico para verificação do cálculo da FAP. Estatísticas de acidente de trabalho por período.  
O gráfico está disponibilizado na biblioteca do produto e pode ser importado através do menu Utilitário| Gráficos | Processos| Importação de Gráfico.  
Nome dos arquivos: 10.80\_RMVitae\_GraficoFAP\_Sql.TotvsGraf 10.80\_RMVitae\_GraficoFAP\_Oracle.TotvsGraf

**Informação Complementar:** Para que serve o FAP? O FAP serve para ampliar a cultura da prevenção dos acidentes e doenças do trabalho, auxiliar a estruturação do Plano Nacional de Segurança e Saúde do Trabalhador - PNSST, reforçar o diálogo social entre empregadores e trabalhadores, tudo afim de avançarmos cada vez mais rumo às melhorias ambientais no trabalho e à maior qualidade de vida.

**Atenção! Possibilidade de cadastrar atestados com continuidade de afastamento!**

Caso necessite cadastrar atestados com continuidade de afastamento, ou seja, atestados que são continuidade um do outro, pode ser utilizado o campo "Data Inicial da Continuidade de Afastamento" presente no cadastro de Atestados.   
Para utilizar este campo deve seguir os seguintes passos:  
1) No sistema Folha de Pagamento deve marcar o parâmetro "Habilita controle manual de continuidade de afastamentos com Atestado Médico".  
2) No momento do cadastro do Atestado, caso o motivo de afastamento seja dos tipos P (Previdência), T (Acidente de Trabalho) e O (Doença Ocupacional), no campo "Data Inicial da Continuidade de Afastamento" será permitido cadastrar uma continuidade de afastamento gerados por atestados do mesmo tipo ou tipos diferentes, inseridos anteriormente, desde que sejam com data anterior à data de início do novo atestado.

**Observação**: Quando marcamos o parâmetro "Habilita controle manual de continuidade de afastamentos com Atestado Médico" e utilizamos a continuidade do afastamento, pelo campo "Data Inicial da Continuidade de Afastamento", o sistema não verifica mais se o motivo do afastamento é igual para realizar o cálculo de dias de atestado. O cálculo dos dias de atestado irá somar os dias do afastamento que inicia a sequência de continuidade (registro Pai), com os dias de afastamento que possuem no campo de relacionamento a informação do registro inicial (Pai). Estes chamados de registros Filhos.  
A soma dos dias deste relacionamento será limitada a 15 dias para a definição do período de Atestado Médico a ser pago pela Empresa ao funcionário, respeitando o intervalo informado no parametrizador da Folha de Pagamento, campo "Dias de carência para afastamento com atestado médico".

Caso o processo, após seguir a sequência de continuidade definida pelo usuário, identifique que o funcionário já tenha atestado pela Previdência para aquela doença, o atestado não será lançado no envelope de pagamento.

 **Retificação do afastamento**  
 Este campo deve ser preenchido quando houver retificação do afastamento temporário.  
 Preenchendo este campo ao gerar o xml  S-2230 a tag origRetif  será preenchida com 1, 2 ou 3

  OBS: Este campo só será exibido caso haja retificação do afastamento já enviado ao eSocial. 

**Tipo do processo:** Preencher com o códigos correspondentes ao tipo de processo:  
 1-Administrativo  
 2-Judicial  
 3-Número de beneficio(NB) do INSS  
Preenchimento obrigatório se o campo Origem da retificação =[2,3]  
Preenchendo este campo ao gerar o xml  S-2230 a tag tpProc será preenchida com 1, 2 ou 3

**Número do processo:**Informar o número de processo de acordo com o tipo de processo cadastrado acima.  
Preenchimento obrigatório se o campo Origem da retificação =[2,3]  
Preenchendo este campo ao gerar o xml  S-2230 a tag nrProc será  preenchida com o número do processo cadastrado.
