---
content_hash: df6a40026904e025466aa9b80cbbf86f5301b1b6c681c368bf7f2a8d61079317
fetched_at: '2026-06-29T00:05:59.643966+00:00'
page_id: '191467596'
product: rm
source: tdn-rm
title: RMFIS00002_02.002 - Roteiro para implantação da ECF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=191467596
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.38 e superiores** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | Parametrização e Geração |
| **Data da publicação** | **:** | 03/07/2015 |

O roteiro abaixo pode ser utilizado como um check list para auxiliar na implantação da ECF.

1. **Ambiente mínimo**: Versão 11.82.38. Devem ser executados os scripts da ECD e ECF.  
   No link () tem mais informações: nome dos arquivos, como baixar, FAQ para execução de scripts, entre outros.  
     
   Para os clientes que estão na versão 12.1, as implementações estão disponíveis a partir do patch **12.1.5.105.**
2. Ajustar Perfil de Usuário para acesso aos novos menus do sistema (Contábil, Fiscal e Integração – Gerador de Saídas).
3. **Gestão Contábil:**
   1. **Plano de Contas Paralelo**  
      1. Criar e importar Plano de Contas Referencial
      2. Realizar associação das Contas Contábeis no Plano Referencial
      3. Criar e importar Estrutura para geração do Registro L210, através dos Planos (**apenas para Lucro Real**)
      4. Mapear as Contas Contábeis na Estrutura do L210 (**apenas para Lucro Real**)  
         <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.planoContaParalelo.aspx>  
           
         Atenção! Os itens 'i' e "ii" acima já foram executados pelos clientes que já efetuaram a geração da ECD pelo sistema.
   2. **Ferramenta de Demonstrações Contábeis** - Criar estrutura de DRE para posterior vinculação ao Evento Tributário da Gestão Fiscal (apenas para Lucro Real).  
      <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.DemonstracaoContabil.aspx>
   3. **Apuração Virtual** – Deve ser parametrizada se o cliente faz transferência de Grupos Contábeis apenas no final do ano e possui apuração trimestral.  
      <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.ApuracaoVirtual.aspx>
4. **Gestão Fiscal**  
   1. **Cadastro de Filiais**  
      Parametrizar o Anexo “Parâmetros da Escrituração Contábil Fiscal”.  
      <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.AnexoFilialParametrosECF.aspx>
   2. **Cadastrar/Ajustar Tributos** (se necessário).
   3. **Obrigações Acessórias**
      1. Importar Tabela Dinâmica da ECF  

         <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.TabelaDin%C3%A2mica.aspx>  
         <http://tdn.totvs.com/pages/viewpage.action?pageId=187831106>
      2. Importar Layout de geração da ECF no Gerador de Saídas
   4. **Obrigações Principais**
      1. Lalur – Parte B
         1. Criação do Plano de Contas
         2. Carga inicial das contas que já são controladas pelo Cliente  
            <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ParteBLalur.aspx>
      2. Evento Tributário:
         1. Criar ou ajustar os Eventos Tributários aplicáveis ao regime de apuração do Cliente.
         2. Inclusão de Lançamentos do Período no Lalur – Parte B
         3. Inclusão de Lançamentos Manuais no Evento Tributário
         4. Criar vigências para os Eventos Tributários  
            <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventosTributarios.aspx>
      3. Período de Apuração:
         1. Criar ou reabrir os Períodos de Apuração de 2014
         2. Encerrar os Períodos de Apuração (após a parametrização do Evento Tributário)
         3. Realizar conferência de todos os valores apurados pelo sistema.  
            <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoImpostosFederais.aspx>
   5. **Geração da ECF**
      1. Importar o arquivo gerado pelo TOTVS Gestão Fiscal no PVA da RFB.
      2. Analisar e sanar possíveis erros de importação.
      3. Alguns Blocos/Registros não são gerados pelo sistema. O cliente deve imputar essas informações no PVA e submeter a Escrituração à validação.
      4. Analisar e corrigir possíveis erros de validação do PVA.  
         <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx>
