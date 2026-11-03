---
content_hash: d6acf2be64558f483add3172bf10234c0268043c6bb148f796f938ece6e494ba
fetched_at: '2026-06-29T00:09:24.072560+00:00'
page_id: '423935245'
product: rm
source: tdn-rm
title: 3825333 FISCAL01-6699 DT - TAF Registros T001, T001AB, T013 - Dados do Contato
type: documentation
url: https://tdn.totvs.com/display/LRM/3825333+FISCAL01-6699+DT+-+TAF+Registros+T001%2C+T001AB%2C+T013+-+Dados+do+Contato
version: 7
---

Tempo aproximado para leitura:**01 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Integração RM x TAF |

**02. SITUAÇÃO/REQUISITO**

Cliente solicita que os dados do Contato - REINF, Classificação Tributária e Ramos de Atividade sejam preenchidos automaticamente na integração RM x TAF

**03. SOLUÇÃO**

Foi modificado o layout de integração com o TAF conforme abaixo.

1. **Registro T001:**
   1. Campo 11 - CLASSTRIB: Foi incluido a opção 7 - Produtor Rural Pessoa Jurídica
   2. Campo 24 - IND\_PROD\_RURAL: Foi ajustado para gerar o valor "1 - SIM" quando o a classificação tributária estiver como Produtor Rural
   3. Campo 13 - NMCTT: O campo passou a ser gerado em branco
   4. Campo 14 - CPFCTT: O campo passou a ser gerado em branco
   5. Campo 15 - FONEFIXO: O campo passou a ser gerado em branco
   6. Campo 16 - FONECEL: O campo passou a ser gerado em brancoFoi Criado um combobox na Tela de Geração dos Registros do TAF\Sub pasta Demais (Parametro 3) para escolher qual será o contato da filial com as opções de CONTADOR ou REPRESENTANTE.  
   Este campo irá determinar qual será a origem da informação para os campos abaixos do registro T001  
     
     
   1. Campo 26 - EMAIL\_CTT\_REINF: Gerado conforme o Campo e-mail do Contador ou Representante. Anexo Cadastro Filial.  
      DFILIAL.EMAILCONTADOR  
      DFILIAL.EMAILREPRES
   2. Campo 27 - NOME\_CTT\_REINF: Gerado conforme o Campo Nome do Contador ou Representante. Anexo Cadastro Filial.  
      DFILIAL.NOMECONTADOR  
      DFILIAL.NOMEREPRES
   3. Campo 28 - CPF\_CTT\_REINF: Gerado conforme o Campo CPF do Contador ou Representante. Anexo Cadastro Filial.  
      DFILIAL.CPFCONTADOR  
      DFILIAL.CPFREPRES
   4. Campo 29 - DDD\_FONE\_REINF: Gerado conforme o Campo DDD do Contador ou Representante. Anexo Cadastro Filial.  
      DFILIAL.DDDCONTADOR  
      DFILIAL. DDDREPRESENTANTE
   5. Campo 30 - FONE\_REINF: Gerado conforme o Campo CPF do Contador ou Representante. Anexo Cadastro Filial.  
      DFILIAL.TELCONTADOR  
      DFILIAL.TELREPRES
   6. Campo 31 - DDD\_CELULAR\_REINF: Gerado conforme o Campo CPF do Contador ou Representante. Anexo Cadastro Filial.  
      DFILIAL.DDDCELCONTADOR  
      DFILIAL.DDDCELREPRES
   7. Campo 32 - CELULAR\_REINF: Gerado conforme o Campo CPF do Contador ou Representante. Anexo Cadastro Filial.  
      DFILIAL.CELULARCONTADOR  
      DFILIAL.CELULAREPRES
2. **Registro T001AB:**
   1. Campo 6 - ID\_VARA: O tamanho do campo foi modificado para 6
3. **Registro T015:**
   1. Campo 44 - COD\_DIPAM: O campo foi adicionado ao layout, mas será gerado em branco
   2. Campo 45 - IND\_ISENCAO\_PREVID: O campo foi adicionado ao layout, mas será gerado em branco

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
