---
content_hash: 2f0c9a501b4c04b726433d2e51201febdd4f00957cea2b750e6ea6a6d71ca406
fetched_at: '2026-06-29T00:08:50.094429+00:00'
page_id: '331862624'
product: rm
source: tdn-rm
title: RMFIS00015_Registro 0035 - Filial SCP
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00015_Registro+0035+-+Filial+SCP
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.x |
| **Ocorrência:** | Geração do Registro 0035 - Filial SCP |
| **Ambiente:** |  |
| **Passo a passo:** | A partir de Janeiro de 2014 a EFD Contribuições deverá ser transmitida separadamente para cada SCP além da transmissão da EFD Contribuições da própria Sócia Ostensiva. Além disso, é necessário a geração do registro 0035 para identificar as SCP´s.    **Cadastro Filial SCP**    É necessário que no cadastro da filial SCP esteja com a opção "Filial é SCP" marcada e a "Filial Sócio Ostensiva" esteja informada.  Cadastro da filial - Anexos/ Dados fiscais        Ao gerar o arquivo da filial Sócio Ostensiva, será gerado o registro 0035 para cada filial SCP vinculada a essa Sócio Ostensiva.  Assim, como determina a legislação, deverá gerar um arquivo separadamente para cada filial SCP.  Ao gerar a EFD para as filiais que são SCP´s serão selecionados os dados somente da filial SCP em questão e será gerado o registro 0035 destacando essa mesma filial para identificação do Fisco.  Trecho do guia pratico sobre o registro 0035:  *Registro de preenchimento obrigatório, quando no campo 13 do Registro “0000” constar o indicador “03”,“04” ou “05”.  No caso de constar no Campo 13 do Registro 0000 o indicador “03” ou “04”, podem ser gerados vários registros “0035”, 01 (um) para cada SCP em que a pessoa jurídica titular da escrituração, participe na condição de sócio ostensivo. No caso de constar no Campo 13 do Registro 0000 o indicador “05”, será gerado apenas 01 (um) registro “0035”, identificando a SCP a que se refere a escrituração em referência.*    **Tela de Geração da rotina**    Na tela de geração da rotina no campo "Indicador da natureza da pessoa jurídica" deverá informar a opção correspondente a filial.  Se a geração do arquivo for para a filial **Sócio Ostensiva**, deverá selecionar a opção 03 ou 04.  Se a geração do arquivo for para a filial **SCP**, deverá selecionar a opção 05. |
| **Observações:** |  |
