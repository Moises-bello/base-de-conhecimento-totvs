---
article_id: 360028440751
category: Gestão de Transportes (TMS)
content_hash: fcd600cc48c0c773fafc886571871ee0892dbb1bbbe01bd4d21b7f2bfbd153ee
fetched_at: '2026-06-28T22:45:27.251040+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Alteração do tomador de serviço no CT-e
  de Substituição
type: support-article
updated_at: '2024-01-16T20:30:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028440751-Log%C3%ADstica-Linha-Protheus-TMS-Altera%C3%A7%C3%A3o-do-tomador-de-servi%C3%A7o-no-CT-e-de-Substitui%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15772873801751)*** Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como efetuar a alteração do **tomador de serviço** no **CT-e - Conhecimento de Transporte Eletrônico** de **Substituição**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O módulo **SIGATMS - Gestão de Transportes** foi atualizado para prever a troca do tomador de serviços na emissão do **CT-e de Substituição,** conforme [AJUSTE SINIEF 8/17](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2017/AJ_008_17) que altera o **AJUSTE SINIEF 09/07**, que institui o **Conhecimento de Transporte Eletrônico** e o **Documento Auxiliar do Conhecimento de Transporte Eletrônico**.  
Para efetuar o processo de alteração do tomador, siga os seguintes passos:

1. Acessar **Atualizações/Transporte/Manutenção Doctos - TMSA500.**
2. Posicione no documento que deseja realizar a substituição e acesse **Outras Ações/Substituição**.
3. Ao abrir a tela clique na pasta **Documento** e pressione **F3** no campo **Devedor - DT6\_CLIDEV** para apresentar os **Clientes**.
4. Escolha o novo **Tomador de Serviços** e clique em **OK.**
5. O campo **Devedor**irá realizar as seguintes validações:
   * O novo tomador de serviços deve constar no conhecimento como: **Remetente**, **Destinatário**, **Consignatário**, **Despachante** ou **Expedidor**.
   * O novo tomador pode não constar no conhecimento original, desde que pertença a uma das empresas originalmente, sendo validado a base do **CNPJ - Cadastro Nacional da Pessoa Jurídica**, e que esteja na mesma **Unidade Federativa** do tomador original.
6. Após seleção do novo tomador, o processo de substituição continua o mesmo, portanto deve-se acessar a opção **Outras Ações/Substit.,** informar o campo **% Substituição** que caso não haja alteração de valores deverá ser **100%**, fazendo com que o novo conhecimento possua o mesmo valor do original.
7. Na pasta **Materiais** verifique se os campos referentes a **Peso, Volume, Valor Mercadoria**e/ou **Unitizadores** estão corretos.
8. Clique em **Confirmar**para confirmar a operação e gerar o novo documento de transporte:
9. Após a conclusão do processo, o documento deverá ser apresentado e transmitido para a **SEFAZ.**
10. A substituição do conhecimento deverá ser transmitida para a **SEFAZ - Secretaria de Estado da Fazenda** utilizando o **Totvs Sped Service - TSS**
11. Para realizar a transmissão do **CT-e de substituição** acesse a opção **Outras Ações/CT-e**.
12. Na tela de parâmetros insira as informações conforme **Documento, Série, Data de Emissão, Status do Documento** e **Tipo de Documento = P**.
13. Selecione o documento e clique no botão **Transmitir.**
14. Após a transmissão e autorização da **SEFAZ**, a substituição foi realizada com sucesso.

**Importante**A partir do CT-e 4.00, será necessário gerar o evento de desacordo vinculado do CT-e original para poder autorizar o CT-e de substituição, passível da **Rejeição 739 - O CTe substituído deve possuir evento de Prestação do Serviço em Desacordo**.  
  
**Saiba mais**Orientações sobre troca do tomador na Substituição do CT-e: [Orientações Consultoria de Segmentos - 3.2 - Tomador Contribuinte do ICMS](https://tdn.totvs.com/pages/releaseview.action?pageId=729239887#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCCeeAnula%C3%A7%C3%A3oeSubstitui%C3%A7%C3%A3odoCTe-3.2TomadorContribuintedoICMS)
