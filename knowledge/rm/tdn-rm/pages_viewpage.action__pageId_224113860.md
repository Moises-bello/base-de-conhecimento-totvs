---
content_hash: fb31be0dfe7d034936c6dd077bf4576d659dd9fd5c938393e8843bb28f0bbf62
fetched_at: '2026-06-29T00:06:24.181616+00:00'
page_id: '224113860'
product: rm
source: tdn-rm
title: RMFIS00003_FECP_FEM - Fundo de Combate a Pobreza e Erradicação da Miséria de
  Minas Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224113860
version: 12
---

Passo a Passo para Parametrização e Geração do Fundo de Combate à Pobreza de Minas Gerais – FEM.

1. **Atualizar a versão da Biblioteca**

* Implementação da EC 87/2015 e NT002/2015 foram realizadas a partir das versões: 
  + BibliotecaRM  11.82.42.116.
  + Versão do Aplicativo TOTVS GESTÃO FISCAL.
* Necessário a execução do Script, disponível na Central de Downloads

* + **SCRIPT\_FEM** (TTWKG7-FEM–CalculoDoFECP-MG.zip)
* Necessário, também atualiza a versão do RMLiber.exe (11.82.42.1).

       2. **Cadastro **Produto****

Implementado no Cadastro Produto| Anexo| Dados Fiscais por UF, o campo "% FECP".

 Este campo será utilizado para o cálculo do Valor do FECP na inclusão de Lançamentos Fiscais.

**3. Parametros Por Filial**  
  

Necessário habilitar o parâmetro "Calcula Fundo de Combate à Pobreza e as Desigualdades Sociais (FECP)"  
  

Gestão Fiscal | Ambiente | Parâmetros |Totvs Gestão Fiscal | 03.02 - Apuração de Tributos| 03.02.01 - ICMS | Apuração. ICMS por Filial

**4.Lançamento Fiscal**

 Conforme a Legislação o % FECP deve ser incluído na Alíquota do ICMS ou Alíquota do ICMS ST, será necessário acrescentar nestas alíquotas o % FCP.

O Cálculo é feito através da Base de Cálculo do ICMS informada na Pasta de Valores do ICMS na inclusão dos itens e ao final somado o Valor do FECP na Situação Tributária do Lançamento Fiscal ao salvar o Lançamento. (Campo Não Editável).  
 Quando não existir percentual no Cadastro do Produto o sistema será utilizado o percentual da Regra de ICMS para o cálculo nos Itens, porem este percentual não será gravado na Situação Tributária do Lançamento Fiscal.  
  

O Campo % FECP do item será originado do % do FECP cadastrado no Anexo Produtos por UF.

**5.Lançamento de Outros Debitos\Credito**

Os lançamentos de Outros\Debito serão gerados automaticamente através do Processo de Inclusão automática para "Gerar Lançamentos Outros Débitos e Créditos do FECP". Este processo somente será habilitado se o parâmetro "Calcula Fundo de Combate à Pobreza e as Desigualdades Sociais (FECP)" estiver habilitado.

 Selecione os períodos dos tributos ICMS e ICMS ST para geração dos lançamentos do FECP/FEM

   
   
   
 Por esta opção será incluído automaticamente até 6 lançamentos de Outros Débitos\Créditos com as seguintes características:   
 **5.1. FECP\Próprio**  
 Tipo de Lançamento: Estorno de Débito  
 Sub Tipo: FECP\FEM ICMS Próprio   
Valor:  Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos Fiscais de saída  com natureza “5.XXX” cuja operação tributária não seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados desabilitado.

**5.2. FECP\Consumidor Final**

Tipo de Lançamento: Estorno de Débito  
 Sub Tipo: FECP\FEM Consumidor Final   
Valor: Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos Fiscais de saída  com natureza “5.XXX” cuja operação tributária não seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados habilitado.

**5.3. FECP\ICMS ST**  
 

Tipo de Lançamento: Estorno de Débito  
 Sub Tipo : FECP\FEM ICMS ST

Valor: Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos fiscais de saída com natureza “5.XXX”, "1.XXX" ou "2.XXX" cuja operação tributária seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados desabilitado.

**5.4. FECP\ICMS ST Consumidor Final**

Tipo de Lançamento: Estorno de Débito  
 Sub Tipo: FECP\FEM ICMS ST\Consumidor Final

Valor:  Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos fiscais de saída com natureza “5.XXX”, "1.XXX" ou "2.XXX" cuja operação tributária seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados habilitado.

**Observação aplica - se ao Fecp Icms - ST**: Para Lançamentos com CFOP "**1**.xxx" ou "**2**.xxx" ser considerado deve ter o Tipo Natureza do ICMS com **(3)FlagICMSNormalSTRetCompra** ou  **(J) - FlagIcmsSTRetidoCompra**

Necessário criar o tipo “**Débito Especial**” no cadastro de Lançamentos outros Débitos/Créditos, este tipo será somente informativo e não afetará a apuração dos tributos ICMS e ICMS ST

**5.5. ICMS**

Tipo de Lançamento: Débito Especial  
 Sub Tipo : FECP\FEM ICMS Próprio

Valor:  Será a soma dos valores dos lançamentos Outros Débitos\Créditos gerados   "1. FECP\FEM ICMS Próprio” e  "2. FECP\FEM Consumidor Final".

**5.6. ICMS ST**

Tipo de Lançamento: Debito Especial  
 Sub Tipo : FECP\FEM ICMS ST   
Valor: Será a soma dos valores dos lançamentos Outros Débitos\Créditos gerados   "3. FECP\FEM ICMS ST” e  "4. FECP\FEM ICMS ST\Consumidor Final”.

**Observações:**

* Os lançamentos com o tipo "Débito Especial" são necessários para correta geração da rotina do Sped Fiscal  nos registros E111 e E220, estes lançamentos não afetam a apuração dos tributos ICMS e ICMS ST.
* Os Lançamentos Outros Débitos e Créditos gerados pelo processo para serem considerados no Sped Fiscal deverá ser informado manualmente o campo "*Código Ajuste SPED*" disponível pela Receita Federal.

**6.Apuração dos Tributos ICMS e ICMS-ST**

Criar os campos "Valor FECP\Próprio" e "Valor FECP\Consumidor Final" na sub pasta apuração, estes campos serão preenchidos ao Encerrar o Período de Apuração e com base nos Lançamentos de Outros Débitos/Créditos do "Tipo: Estorno de Debito". e SubTipo: FECP ICMS Próprio e FECP Consumidor Final.

 

As guias serão geradas automaticamente utilizando os valores dos campos  "Valor FECP\Próprio" e "Valor FECP\Consumidor Final"  do período.

**7. Importação/Exportação do Lançamento Fiscal TXT**

Foi disponibilizado o campo % FECP *DITEM.PERFECPITEM com tamanho 15* para importação/exportação.

**8. Escrituração de Lançamentos Fiscais**

No Processo de Escrituração de Lançamentos Fiscais o sistema irá calcular automaticamente o Valor do FECP por Item, quando  
 o Lançamento for uma Saída Interna ou uma Saída Interestadual com a opção "Operação Destinada a Consumidor Final" marcada e o Item estiver com % de FECP preenchido na Base, para o Estado ao qual o Lançamento está sendo criado.  
 Os Valores dos Itens serão somados e gravados na Situação Tributária do Lançamento Fiscal.
