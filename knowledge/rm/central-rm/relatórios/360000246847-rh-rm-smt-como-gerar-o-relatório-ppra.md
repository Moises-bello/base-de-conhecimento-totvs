---
article_id: 360000246847
category: Relatórios
content_hash: 314aafce068a2f5a6d5f47cf996fa69cae349510ff41b8c7afef46fde47d289a
fetched_at: '2026-06-28T22:47:43.490913+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: RH - RM - SMT - Como gerar o Relatório PPRA
type: support-article
updated_at: '2025-09-25T14:50:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000246847-RH-RM-SMT-Como-gerar-o-Relat%C3%B3rio-PPRA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036337767063) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como gerar o relatório PPRA(Programa de Prevenção de Riscos Ambientais)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - A partir da versão 11.80  
  
**Solução**Para geração do relatório, basta seguir os passos abaixo:

1. **Importar estrutura do relatório:** A estrutura do relatório fica disponível book, que se encontra no caminho C:\totvs\CorporeRM\ObjetosGerenciais\Relatórios. E importe o relatório RHUREL0002 - PPRA\_ORA ou RHUREL0003 - PPRA\_SQL, observando o banco de dados (Oracle / SQL). No link abaixo segue o documento com o passo a passo de como realizar o processo de importação:   
    [TOTVS RH - Linha RM - SMT - Importação de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409650455703-TOTVS-RH-Linha-RM-SMT-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios)
2. **Criar tipo de Relatório:** Acesse o menu**Relatórios | Tipos de Relatório** e crie ou edite um tipo desejado e marquem tipo PCMSO e salve.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193430858519)
3. **Gerar itens do relatório:** Após salvar o tipo criado, acesse a opção**Anexos | Itens de Relatório** e, valide se há registros no anexo, caso tenha os exclua.    
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193484768151)  
     
     
   - Selecione tipo criado e acesse a opção  Processos > Gerar modelo de PPRA, e ao aparecer a mensagem *'Deseja inserir automaticamente os itens de modelo para este tipo?'***,**clique em**sim,**Após executar o processo, clique no botão atualizar, para carregar os itens.   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193430869783)
4. **Geração do relatório:** Para gerar o relatório acesse o menu **Relatórios | Relatórios de Segurança** e clique em novo. Preencha os campos Cod Relatório; Data Inicio; Data Fim; Descrição; Cod Tipo Relatório; Cod Local de Trabalho e salve.    
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193430871703)  
     
   **Importante**  
   Como padrão, o sistema **disponibiliza um modelo de PPRA baseado em local de trabalho e a a avaliação e medição de riscos deverão ser realizadas por lotação.** Lembrando que cada empresa deve adaptar este modelo a sua própria realidade.
5. Após salvar, clique guia **Gerar | Visualizar** e cliquei no botão **Gerar Relatório** e depois de gerado clique no botão **Visualizar Relatório.**  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193484782487)

**Saiba mais**

Para maiores informações sobre as informações que são levadas no relatório  basta acessar os links:

[Como fazer o PPRA](https://tdn.totvs.com/display/public/LRM/Como+Fazer+PPRA)

[Relatório PPRA](https://tdn.totvs.com/pages/releaseview.action?pageId=107382544)
