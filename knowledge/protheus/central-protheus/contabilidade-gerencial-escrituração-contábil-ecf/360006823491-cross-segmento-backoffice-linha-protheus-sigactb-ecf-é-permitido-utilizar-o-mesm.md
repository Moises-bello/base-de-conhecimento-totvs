---
article_id: 360006823491
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 03b1d575113b37394be181c056f7b5ed564e74fdad607cf619a21e61cefa854f
fetched_at: '2026-06-28T22:40:47.344984+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - É permitido utilizar o
  mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)? '
type: support-article
updated_at: '2022-07-12T18:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD
---

**Dúvida**

É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus  – SIGACTB – A partir da versão 11.80  
  
**Solução**

**Não**, as informações do Balanço Patrimonial (Registros  L100, P100 e U100) e Demonstrativo de Resultado ( Registros L300, P150 e U150) devem ser demonstrados com as mesmas nomenclaturas existentes no Manual de Orientação do ECF.

Para apoio na configuração foi disponibilizado o modelo das visões gerenciais necessárias para a extração dos dados.

[Arquivos Modelos - Plano Referencial / Visões Gerenciais](http://tdn.totvs.com/pages/releaseview.action?pageId=189314312)

[Veja como Importar a Visão e Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)

# [Dúvidas Frequentes do ECF - Escrituração Contábil](http://tdn.totvs.com/pages/releaseview.action?pageId=187534278)

Veja que o modelo de Visão gerencial disponibilizada possui a conta referencial no campo "Enti Gerenc" , se o campo não estiver preenchido com a conta referencial será apresentado erro na integração com o TAF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007000652/mceclip0.png)

* Para gerar o Balanço Patrimonial (Registros  L100, P100 e U100) e Demonstrativo de Resultado ( Registros L300, P150 e U150) o sistema considera a visão gerencial informada  ou caso **não** informe a visão gerencial ,o sistema **considera o plano referencial amarrado ao plano de contas**

Reg [L100          CSC / CSK         T088AA quando **não** utilizado Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054165034-MP-SIGACTB-ECF-L100-COMO-GERAR?source=search)o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg [L100          CSD / CSE         T088AA quando utilizado Visão Gerencial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054165034-MP-SIGACTB-ECF-L100-COMO-GERAR?source=search)  
Reg [L300          CSC / CSK         T088AD quando **não** utilizado Visão Gerencial,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search) o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg [L300          CSD / CSE         T088AD quando utilizado Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search).   
Reg [P100          CSC / CSK         T092AA quando **não** utilizado Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033885453-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-P100-COMO-GERAR-?source=search),o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg [P100          CSD / CSE         T092AA quando utilizado Visão Gerencial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033885453-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-P100-COMO-GERAR-?source=search)   
Reg [P150          CSC / CSK         T092AC quando **não** utilizado Visão Gerencial,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033364654-MP-SIGACTB-ECF-P150-COMO-GERAR-?source=search)o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg [P150          CSD / CSE         T092AC quando utilizado Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033364654-MP-SIGACTB-ECF-P150-COMO-GERAR-?source=search).   
Reg [U100          CSC / CSK         T094AA quando **não** utilizado Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search), o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg [U100          CSD / CSE         T094AA quando utilizado Visão Gerencial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)   
Reg [U150          CSC / CSK         T094AB quando **não** utilizado Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search),o sistema irá considerar a amarração do plano de contas com o plano referencial   
Reg [U150          CSD / CSE         T094AB quando utilizado Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search).

**Para conciliação dos saldos**

* **Caso esteja utilizando**visão gerencial Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR500,CTBR040 ) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado ,  será necessário avaliar a configuração da visão gerencial
* **Caso Não utilizando**visão gerencial verifique a amarração do plano referencial , veja se ao emitir relatórios relatórios Plano ref. X plano de contas (CTBR025 ,CTBR404,CTBR049) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado,  será necessário avaliar a  amarração da conta contabil com a conta referencial

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)

Caso não utilize o modelo de visão gerencia disponibilizado pela totvs serão  ocasionados os erros abaixo na integração com o TAF, pois o sistema confere se a entidade informada nos campos CVF\_CONTAG, CVF\_CTASUP , CTS\_CONTAG e CTS\_CTASUP existe no campo do TAF CHA\_CODIGO

[MP - SIGACTB - ECF - ( CAQ\_REGECF ) somado ao valor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006649692-MP-SIGACTB-ECF-CAQ-REGECF-somado-ao-valor?source=search)

[MP - SIGACTB - ECF -O valor '01' informado na coluna 2 para o campo ID Conta Referencial ( CEH\_IDCODC ) não existe na base de dados.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006909511-MP-SIGACTB-ECF-O-valor-01-informado-na-coluna-2-para-o-campo-ID-Conta-Referencial-CEH-IDCODC-n%C3%A3o-existe-na-base-de-dados-?source=search)

[MP - SIGACTB - ECF - ERRO: Registro \_ECF(CAG\_TABECF) Conta Referencial \_ (CAG\_CTAREF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004876291-MP-SIGACTB-ECF-ERRO-Registro-ECF-CAG-TABECF-Conta-Referencial-CAG-CTAREF-?source=search)

[MP - SIGACTB - ECF -o campo Tabela Registro ECF(CAE\_TABECF)somado ao valor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006780671--MP-SIGACTB-ECF-o-campo-Tabela-Registro-ECF-CAE-TABECF-somado-ao-valor-?source=search)

Tabela CHA é uma autocontida que é atualizada pelo desenvolvimento do TAF com base [Tabelas Dinâmicas e Planos de Contas Referenciais(Receita)](http://sped.rfb.gov.br/pasta/show/1644)
