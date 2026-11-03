---
article_id: 10755484313751
category: Financeiro
content_hash: abcd04afb1dd06146a45ddc4ac5f2fc77eb799f84179b938f388961592abcbf8
fetched_at: '2026-06-28T22:38:01.078324+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como testar o Certificado
  Digital Modelo A1, antes de Importar ao Protheus
type: support-article
updated_at: '2023-01-25T23:14:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10755484313751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-testar-o-Certificado-Digital-Modelo-A1-antes-de-Importar-ao-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:09:00 min**

**Dúvida**Como testar o Certificado Digital Modelo A1 antes de Importar no Protheus?

**Ambiente**

Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA710- Todas as versões

**Solução**

Para realizar o Teste com o Certificado Digital modelo A1 é necessário que tenha o arquivo com a extensão .PFX juntamente com a senha criada na emissão do certificado.

**![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10754656502039)**

Clique no arquivo 2x para seguir com os passos da instalação e manter o campo abaixo preenchido como **"Usuário Atual"** e clicar no avançar

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10754769163927)

Selecione o diretório do arquivo .PFX e Avançar

![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10754893760023)

Insira a senha do arquivo e marcar as opções **"Marcar esta chave como exportável"** e **"Incluir todas as propriedades"**

![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10754946751767)

Não é necessário definir um repositório para a instalação do certificado, deve seguir conforme o exemplo abaixo e Avançar

**![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10755046365847)**

Clique em concluir para finalizar a instalação do Certificado.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10757622786711)

Acesse o menu iniciar o Windows e digitar **"Serviços"**

**![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10755331307287)**

Para que o Sistema Operacional Windows reconheça o certificado de forma automática após instalação, é necessário que o serviço de **Propagação de Certificado** esteja com o **"Status"** Em Execução e **"Tipo de Inicialização"**Automático (Inicio do gatilho), conforme o exemplo abaixo:

**![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10755195617303)**

Abra o navegador de internet (preferencialmente o Google Chrome) e digitar Portal e-CAC: [Clique aqui](https://cav.receita.fazenda.gov.br)

**![7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10755405607831)**

Clique na opção **"Entrar com gov.br"**

**![8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10755470797207)**

Ao carregar a tela de Identificação clicar na opção **"Seu Certificado Digital"**

**![9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10755525661719)**

Selecione o Certificado digital que será apresentado em tela e clicar no **OK**.

Ao realizar esse procedimento, irá carregar todos os serviços do Site da Receita e o Certificado Digital que demonstra estar apto para uso no **Protheus.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10757506234007)

**Importante**

* Esse processo de Teste do Certificado Digital, por padrão é utilizado pelas Autoridades Certificadoras.
* Para o uso do certificado no Protheus, o arquivo deve conter a extensão .PFX, e o tamanho inicial do arquivo deve ser 7KB (Modelo A1).
* O Protheus irá reconhecer apenas certificado válidos dentro do período de uso, não sendo possível comunicar com certificados expirados (Vencidos).

**Importante**

Caso encontre algum erro ou dificuldade sobre o processo de validação/instalação do Certificado Digital no sistema operacional, é recomendado que acione a Autoridade Certificadora emissora do certificado para um acompanhamento sobre o processo.

**Saiba mais**<https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087>
