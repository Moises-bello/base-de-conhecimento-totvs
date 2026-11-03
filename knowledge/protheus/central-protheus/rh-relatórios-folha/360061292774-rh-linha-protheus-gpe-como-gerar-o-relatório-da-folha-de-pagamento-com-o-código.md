---
article_id: 360061292774
category: RH - Relatórios Folha
content_hash: fd22595de03352c3611d91126c4009fae4e5e60a54ca6b698b7893ebb2bba7ad
fetched_at: '2026-06-28T22:43:17.470039+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o relatório da Folha de Pagamento com
  o código de CBO dos funcionários
type: support-article
updated_at: '2024-08-28T17:34:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061292774-RH-Linha-Protheus-GPE-Como-gerar-o-relat%C3%B3rio-da-Folha-de-Pagamento-com-o-c%C3%B3digo-de-CBO-dos-funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25943053542935) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como gerar o **Relatório da Folha de Pagamento** com o código de **CBO - Código Brasileiro de Ocupações** dos funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para que seja gerada a informação de **CBO**, será necessário utilizar o **Relatório da Folha de Pagamento Personalizado - GPER106**, uma vez que o **Relatório da Folha de Pagamento - GPER040 não apresentada essa informação**, o Relatório Personalizável permite selecionais quais informações serão exibidas nos relatórios gerados pelo Sistema.  
Para que seja possível utilizar relatório personalizados, deve ser modificado o conteúdo do parâmetro **MV\_TREPORT** para 2 - Utiliza ou 3 - Pergunta se utiliza.  
  
Para inserir a informação do código de CBO, siga os procedimentos abaixo:  
  
**1.** Acessar o Relatório Personalizável da **Folha de Pagamento (GPER106)**, que se encontra em **Relatórios > Periódicos > Folha de Pagamento**. Se você optar pelo conteúdo 3 no parâmetro **MV\_TREPORT**, o Sistema exibirá uma mensagem perguntando se você deseja **Imprimir Relatório Personalizável**, clique **Sim**;  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002689001)  
  
**2.** Será aberta a janela do Relatório, clicando em **Outras Ações,** você tem acesso aos **Parâmetros** para gerar o Relatório e ao item **Personalizar**, você deve clicar nele, para que seja possível criar um layout personalizado;  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103688713)  
  
**3.** A tela abaixo será exibida, clique no **+** localizado ao lado de **Folha de Pagamento** para que as abas abaixo dela sejam demonstradas, a informação que precisamos gerar pertence ao Funcionário, portanto deve você deve selecionar o item **Filial/Funcionário**;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101529914)  
  
**4.** Depois de selecionar o item **Filial/Funcionário** clique na **barra Células**, para que seja possível selecionar os campos desta consulta, que você deseja gerar no Relatório Personalizado;  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103686393)  
  
**5.** Os botões de **Seta** permitem incluir e/ou excluir campos a serem exibidos no relatório, apesar da Rotina **Funcionários - GPEA010** exibir o código de CBO no **campo C.B.O. 2002 (RA\_CODCBO)**, o conteúdo apresentado não é gravado na **Tabela SRA**, desta forma o campo existente é apenas uma demonstração do que esta cadastrado para a função definida ao funcionário pelo campo **Cod. Função (RA\_CODFUNC)** que por sua vez efetua a busca na rotina **Funções - GPEA030**, onde é possível relacionar um CBO para a função através do campo **CBO 2002 (RJ\_CODCBO**).  
Sendo assim **será necessário criar uma fórmula** para fazer esse relacionamento e exibir o código de CBO gravado na **Tabela SRJ**, clique duas vezes no **botão Fórmula**, destacado na imagem abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002647342)  
  
**6.** Insira a fórmula fCodCBO(SRA->RA\_FILIAL,SRA->RA\_CODFUNC,dDataBase) na caixa que foi aberta,  depois clique em **Confirmar**.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002687801)  
  
**7.** Informe um título para este **campo Fórmula** que foi criado, no **campo Máscara** insira o **conteúdo @!**, como demonstrado na imagem abaixo. Em seguida clique em **Salvar**, para gravar o Layout que esta sendo criado, você pode salvar o o mesmo para todos ou apenas para o seu usuário. ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002687941)  
  
**8.** Selecione o Layout criado no item anterior, preencha os **Parâmetros** localizado em **Outras Ações** e clique em **Imprimir** para gerar o Relatório  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101532514)  
  
**9.** Será exibido um alerta informando que não é possível exibir campos customizados, em seguida o relatório será gerado com a informação do CBO vinculado ao funcionário.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002688961)  
  
**Saiba Mais:**  
[MP - GPE - Como habilitar relatórios personalizáveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038720174-MP-GPE-Como-habilitar-relat%C3%B3rios-personaliz%C3%A1veis)

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
