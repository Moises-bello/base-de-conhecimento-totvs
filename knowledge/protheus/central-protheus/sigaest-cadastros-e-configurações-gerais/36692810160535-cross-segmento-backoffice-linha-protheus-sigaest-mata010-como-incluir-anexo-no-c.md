---
article_id: 36692810160535
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 072df359d20af63b00650f473b3b0d94dc340d00b46e79fcccd625b6607bcb3d
fetched_at: '2026-06-28T22:39:07.921274+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como incluir
  anexo no cadastro de produto?
type: support-article
updated_at: '2025-12-01T18:39:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36692810160535-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-incluir-anexo-no-cadastro-de-produto
---

É possível vincular anexos, como boletins técnicos, ao cadastro de produtos no TOTVS Protheus através do Banco de Conhecimento. O processo envolve cadastrar o documento no Banco de Conhecimento, vinculá-lo ao produto via módulo SIGAEST e importar o arquivo usando o Wizard. A consulta do anexo é feita diretamente pelo cadastro do produto.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36692837478423) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possivel incluir, anexos dentro do cadastro de produto? Como por exemplo, um boletim das informações tecnicas do item?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
É compreensível a necessidade de vincular documentos, como bulas ou fichas técnicas, diretamente ao cadastro de produtos. Embora o sistema (Rotina MATA010) não possua uma função nativa de anexo direto, é possível realizar essa amarração de forma eficaz por meio do **Banco de Conhecimento**.

Este método permite que você armazene e gerencie documentos centralmente, vinculando-os a produtos específicos.

### **1. Cadastro do Banco de Conhecimento**

O primeiro passo é registrar o seu anexo na base que centraliza a documentação.

* **Acesso:** Acesse o módulo **SIGAEST > Atualizações > Cadastros > Banco de Conhecimento.**
* **Inclusão:** Inclua um novo registro e preencha os dados necessários para identificar o documento (ex: "Bula do Medicamento XYZ").
* **Salvar:** Salve o registro.

### Screenshot_5.png **2. Vinculação do Anexo ao Cadastro de Produto**

Após criar o registro no Banco de Conhecimento, você irá vinculá-lo ao produto desejado:

* **Acesso ao Produto:** Acesse o módulo **SIGAEST > Atualizações > Cadastros > Produto.**
* **Seleção:** Selecione o produto desejado na listagem.
* **Ação:** Clique em **"Outras Ações" > "Relacionadas" > "Conhecimento"**.

![Captura de tela 2025-12-01 125227.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36693641612823)

### **3. Importação do Documento (Anexo)**

Com a tela de **"Vínculo - Banco de Conhecimento"** aberta, realize a importação do arquivo:

* **Wizard:** No lado direito da tela, clique em **"Outras Ações" > "Wizard"**.
* **Seleção do Arquivo:** Selecione o local onde o arquivo (a bula, o boletim, etc.) está salvo para que seja importado para dentro do Banco de Conhecimento.

  > **💡 Boa Prática:** Sugerimos manter uma pasta salva com todos os documentos a serem anexados. Isso garante que, ao atualizar o documento na pasta de origem, o sistema reflita automaticamente essa atualização no anexo.
* **Finalização:** Finalizado o processo do *Wizard*, o documento estará vinculado.

![Captura de tela 2025-12-01 125458.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36693641614103)

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36693641617303)

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36693658074903)

### **4. Consulta do Anexo**

Para consultar o documento a partir do cadastro do produto:

* **Acesso:** Na tela de **"Vínculo - Banco de Conhecimento"** (acessada pelo produto), selecione o registro do anexo.
* **Visualização:** Clique em **"Abrir"** para visualizar o documento anexado.

![Captura de tela 2025-12-01 125814.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36693735373847)

### 

### **5. Uso e conceito do Banco de conhecimento**

[Framework - Linha Protheus - Finalidade do Banco de Conhecimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049120753-Framework-Linha-Protheus-Finalidade-do-Banco-de-Conhecimento)

**Saiba mais:**

[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)
