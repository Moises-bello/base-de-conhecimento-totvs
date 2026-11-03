---
content_hash: fb355a33a8a17ad6f4921c85d396bb88e81ccca3d13cb48a126ca73557bc969e
fetched_at: '2026-06-29T00:09:18.124668+00:00'
page_id: '421388675'
product: rm
source: tdn-rm
title: Visualizar Informações dos Boletos Impressos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388675
version: 14
---

Permite que o usuário armazene na base de dados, as informações contidas nos boletos que foram impressos utilizando o RM Reports. Depois de armazenado, esse conteúdo pode ser visualizado, formando assim um histórico de boletos.

Para que se visualize estas informações do histórico de boletos deve-se respeitar as parametrizações e execução dos passos abaixo:

* Acessar Serviços Globais | Segurança | Perfil assim selecione o perfil do usuário, na aba “Acesso a Menus” de permissão para as seguintes linhas:

1. [07.04.03.04] Visualizar Informações dos Boletos Impressos: libera a visão das informações dos boletos impressos.
2. [07.04.03.04.01] Visualizar Dados Extraídos do Boleto: libera a visualização dos dados que foram extraídos do boleto selecionado na visão de boletos impressos.
3. [07.04.03.04.02] Extração de Dados do Boleto: libera processo de extração dos dados do boleto na visão de boletos impressos.
4. [07.04.03.04.03] Visualizar Boleto: libera a visualização, em PDF, do boleto selecionado na visão de boletos impressos.

* Cadastrar lançamento a receber;

* Gerar novo boleto ou incluir o lançamento cadastrado em um já existente;

* Gerar IPTE e código de barras para o boleto através do processo em Boleto | Processos | Processo de geração de código de barras.

* Imprimir o boleto cadastrado através do processo em Boleto | Processos | Impressão de Boleto.

* Acessar a visão de boletos impressos no menu Utilitários | Outros | “Mais...” | Visualizar Informações dos Boletos Impressos;

* Executar processo "Visualizar Boleto";

* Selecionar o boleto impresso e executar o processo "Extrair Dados do(s) Boleto(s)".

Para visualizar os dados extraídos do boleto, basta acessar: Utilitários | Outros | “Mais...” | Visualizar Informações dos Boletos Impressos | Anexos | Dados Extraídos do Boleto.

**Observação:**

* Para correto funcionamento do processo executado no último passo acima é necessário que o relatório utilizado para impressão do boleto no quinto passo esteja corretamente configurado e gerando todas as informações pertinentes no boleto.
* Se dois boletos foram visualizados/impressos em conjunto ao visualizar usando este processo ambos também estarão juntos.
