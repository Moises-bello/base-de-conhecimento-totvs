---
content_hash: c3afff2804e15396e7f329f6af96976cc3a29c3e9c824d46eb194f7ab703e3ca
fetched_at: '2026-06-29T00:09:27.945224+00:00'
page_id: '423938582'
product: rm
source: tdn-rm
title: Moeda funcional Diferente da Moeda Nacional (R$) 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938582
version: 3
---

As pessoas jurídicas obrigadas a transmitir, via Sped, a escrituração em moeda funcional diferente da moeda nacional e que, nos termos do art. 156 da Instrução Normativa RFB no 1.515, de 24 de novembro de 2014, são obrigadas a transmitir, para fins tributários, escrituração com base na moeda nacional, deverão preencher o campo identificação de moeda funcional do registro 0000 (0000.IDENT\_MF) com "S" (Sim) constante no leiaute 4.

Quando 0000.IDENT\_MF for igual a "S", os campos já existentes nos registros I155, I157, I200, I250, I310 e I355 deverão ser preenchidos com os valores baseados em moeda nacional, atendendo ao disposto nos artigos 155 e 156 da Instrução Normativa RFB no 1.515/2014.

Além disso, a pessoa jurídica deverá criar campos adicionais auxiliares no arquivo da ECD, por meio do preenchimento do registro I020, conforme abaixo, para informar os valores da contabilidade em moeda funcional, convertida para reais conforme regras previstas na legislação societária.

Este controle será disponibilizado a partir do layout 4.0 do SPED Contábil  
   
**Impactos e Alterações no Módulo TOTVS Gestão Contábil**  
No módulo TOTVS Gestão Contábil as informações referentes a moeda funcional serão controladas em contas contábeis especificas, ou seja, o usuário deverá:

* Cadastrar contas especificas para controlar as variações cambial;
* Realizar o lançamento das variações cambial nestas contas;
* Parametrizar o sistema para controlar moeda funcional;
* Identificar nos parâmetros as contas contábeis que controlam os valores com efeitos em moeda FUNCIONAL.

Exemplo: Caso haja alguma variação cambial em determinada operação ou conta deve-se calcular este valor e aplica-lo na conta criada para controlar a variação em contra partida esse movimentação deve impactar diretamente o PL em uma outra conta para ajuste.

**Parâmetros do sistema**  
Foi habilitado em "Rotinas Legais" uma pasta chamada "Moeda Funcional" nesta pasta teremos as seguintes informações:

* Opção "Habilitar Controle de moeda funcional no SPED Contábil?": Indica que na geração do SPED Contábil o sistema irá gerar as informações conforme o manual do SPED Contábil considerando a moeda funcional.

* Identificação das Contas Contábeis que controlam a moeda funcional: Houve a criação de um cadastro neste parâmetro para que o usuário selecione  as contas contábeis que controlam os efeitos em moeda funcional.

**Processamento do SPED Contábil**  
Quando o parâmetro  "Habilitar Controle de moeda funcional no SPED Contábil?" estiver marcado, o registro 0000, no campo  0000.IDENT\_MF deverá ser gerado com "S".  
   
**Regras**  
 Regra 1: As informações (movimentações/saldo) referente as contas contábeis identificadas nos parâmetros (Moeda Funcional) terão seus valores apresentados somente nos campos criados pela Receita Federal para controlar os valores com efeitos em moeda FUNCIONAL( \_AUX ), ou seja, para informações destas contas nos registros destacados abaixo os campo já existentes nas versões anteriores estarão com os valores zerados, e somente os campos auxiliares terão valores preenchidos.

Segue abaixo os registros impactados por esta regra, esses registros terão campos que serão preenchidos com o valores processados para as contas contábeis parametrizadas para controlar moeda funcional:

* I155: DETALHE DOS SALDOS PERIÓDICOS;
* I157: TRANFERÊNCIA DE SALDOS DE PLANO DE CONTAS ANTERIOR;
* I200: LANÇAMENTO CONTÁBIL;
* I250: PARTIDA DO LANÇAMENTO;
* I310: DETALHES DO BALANCETE DIÁRIO (somente para pessoas jurídicas que fazem balancetes diários);
* I355: DETALHES DOS SALDOS DAS CONTAS DE RESULTADO ANTES DO ENCERRAMENTO.  
     
  Observações:
* Foram criados campos auxiliares(AUX) nos registros citados acima, estes devem refletir os valores em moeda funcional. Os campos já existentes no registro representam os valores reconhecidos e mensurados na moeda nacional. Ambos os campos devem ser registrados em reais (R$);
* As informações (movimentações/saldos) processadas para as contas que controlam a variações referente a moeda funcional não irão refletir nas demonstrações (registros do bloco J, J100 e J150), ou seja, ao conferir o Balanço (J100) ou DRE (J150) os valores referente a estas contas não podem constar e não podem ser processados nestes registro (valores em moeda funcional não podem afetar o Balanço ou DRE).

Regra 2: Todos os campos que forem gerados nos registros relatados acima (Regra 1) deverão ser identificados no registro I020.

Exemplo de Preenchimento do registro I020 (Campos adicionais): |I020|I310|06|VAL\_DEB\_AUX|TOTAL DOS DEBITOS DO DIA|N| Campo 01 – Tipo de Registro: I020 Campo 02 – Código do Registro que Recepciona o Campo Adicional: I310 Campo 03 – Número Sequencial do Campo Adicional: 06 Campo 04 – Nome do Campo Adicional: VAL\_DEB\_AUX Campo 05 – Descrição: Total dos débitos do dia em moeda que não reflita os efeitos de moeda funcional. Campo 06 – Indicação do Tipo de Dado: N (Numérico)  
   
Observação:  
Os registros são gerados conforme a forme de escrituração e em alguns casos são opcionais, com isso deverá constar no registro I020 somente informações de registros efetivamente gerados no arquivo final da ECD.

**Processamento da ECF**  
Durante o processamento da ECF as movimentações referentes as contas contábeis parametrizadas para controlar os valores com efeito na moeda funcional não devem ser consideradas, ou seja, não devem refletir nos registros K155 e K355, no entanto devem ser consideradas no registro J050

Veja Também

* [Consultoria Tributária - Moeda Funcional novos registros na ECD](http://tdn.totvs.com/pages/releaseview.action?pageId=232821297)
* [CPC02 (R2) - Efeitos das mudanças nas taxas de câmbio e conversão de demonstrações contábeis](http://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=9)
