---
content_hash: 08a02100b961ad24de80574489a848f3eff78b5778b89c5dbb0f5572ed198286
fetched_at: '2026-06-29T00:12:02.697075+00:00'
page_id: '90277102'
product: rm
source: tdn-rm
title: Acesso à Base Vazia para Clientes Corporativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=90277102
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                     **Versão:**11.XX |
| **Processo** | **:** | License Server |
| **Subprocesso** | **:** | Acesso à Base Vazia para Clientes Corporativos |
| **Data da publicação** | **:** | 04/11/2013 |

**Acesso à Base Vazia para Clientes Corporativos em Fase de Implantação**

Caso o License Server já esteja devidamente instalado e configurado com os arquivos de licença que contemplam os CNPJ's do cliente cadastrados junto à Totvs, e o erro abaixo seja exibido:

Erro: (-10008) - O Licence Server está rodando no modo corporativo, entretanto o CNPJ 21.867.387/0001-58 não está cadastrado para o uso de licenças corporativas.

**Siga os passos abaixo:**

Na tela de Configuração do License Server, à direita, selecione o menu "Exportar CNPJ / CPF / CEI":

Na tela seguinte selecione o menu novo:

Selecione a coligada 1 e clique em Editar:

Nesta edição informe todos os dados do seu cliente, inclusive o CNPJ, salve e saia por completo do sistema.

Quando o login for realizado novamente, o RM deve identificar o CNPJ novo que é o mesmo dos arquivos de licenças.

**Obs.:** Outra opção para acessar a base de dados vazia é, na Janela de Configuração do License Server, selecionar a opção SHIFT + F6, será exibida a tela para inserir CNPJ e a Chave de Inicialização. Essa informação está disponível na Nota Fiscal do cliente e libera o Sistema para Uso por 15 dias.

Após logar no Sistema acesse o cadastro de coligadas e preencha as informações com os dados da empresa:

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
