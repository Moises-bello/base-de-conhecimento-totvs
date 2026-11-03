---
article_id: 4404129994135
category: Relatórios
content_hash: 0724587b349500f4c4643f004a06720e53dbb9c0770d6c7241c703f66498e20e
fetched_at: '2026-06-28T22:47:43.458698+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: RH - RM - SMT - Como gerar o Relatório PCMSO
type: support-article
updated_at: '2025-04-22T16:34:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404129994135-RH-RM-SMT-Como-gerar-o-Relat%C3%B3rio-PCMSO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036032107543) Tempo aproximado para leitura: 00:02:30 min  
  
Dúvida**Como gerar o relatório PCMSO(Programa de Controle Médico de Saúde Ocupacional)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - Todas as versões  
  
**Solução**

Para gerar o relatório, siga os passos abaixo:

1. **Importar estrutura do relatorio:** A estrutura do relatorio fica disponível no book, que se encontra no **RM** | **Gestão** | **TOTVS Compartilhamento** e procure pela estrutura **RHUREL0007 - PCMSO**, observando sempre o banco de dados (Oracle / SQL).  
   No link abaixo segue o documento com o passo a passo de como realizar o processo de importação:  [RH - RM - SMT - Importação de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409650455703)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006849046935)
2. **Criar tipo de Relatório:** Acesse o menu **Relatórios** | **Tipos de Relatório,** crie ou edite um tipo desejado e marque a opção do tipo **Saúde**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006863430551)
3. **Gerar itens do relatorio:** Após salvar o tipo criado, acesse a opção **Anexos** | **Itens de Relatório** e, valide se há registros no anexo, caso tenha os exclua.   
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006849057559)  
     
     
   - Selecione tipo criado e acesse a opção **Processos** | **Gerar modelo de PCMSO**, e ao aparecer a mensagem *'Deseja inserir automaticamente os itens de modelo para este tipo?'***,** clique em **sim,** Após executar o processo, clique para atualizar a visão para que os itens sejam carregados.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006863435671)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006849064855)
4. **Geração do relatório:** Para gerar o relatório acesse o menu **Relatórios** | **Relatórios de Saúde** e clique em novo. Preencha os campos **Cód Relatório**; **Data Inicio**; **Data Fim**; **Descrição**; **Cód Tipo Relatório**; **Cód Local de Trabalho**; **Cód Seção** e **Cód. Função** e salve.   
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006849066647)  
     
   **Importante**  
   Como padrão, o sistema **disponibiliza um modelo de PCMSO baseado em local de trabalho e a a avaliação e medição de riscos deverão ser realizadas por lotação.**   
   Lembrando que cada empresa deve adaptar este modelo a sua própria realidade.
5. Após salvar, clique na guia **Gerar** | **Visualizar** e vá em **Gerar Relatório**. Após gerar, clica na opção **Visualizar Relatório.**  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006849070231)

**Saiba mais**Para maiores informações, acesse:

- [Relatório PCMSO](https://tdn.totvs.com/pages/viewpage.action?pageId=120783929)

- [Roteiro Relatório PCMSO](https://tdn.totvs.com/pages/releaseview.action?pageId=452719856)

- [Como fazer PCMSO](https://tdn.totvs.com/display/LRM/Como+Fazer+PCMSO)
