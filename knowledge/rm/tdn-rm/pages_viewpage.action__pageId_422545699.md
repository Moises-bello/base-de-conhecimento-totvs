---
content_hash: bc51422c0aaba8e285f2942146698b9b4bbba558d30bf7c2426b46504b87979a
fetched_at: '2026-06-29T00:09:20.496378+00:00'
page_id: '422545699'
product: rm
source: tdn-rm
title: Exercício Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545699
version: 22
---

# Conteúdo

Conteúdo

# 1. Sobre

O Exercício Fiscal foi criado para delimitar a vigência dos Códigos Fiscais de Operações e Prestações (CFOP), inclusive permitindo a mudança da máscara do Código, conforme já determinado pelo fisco no passado.

# 2. Parâmetro Natureza Global

Através do parâmetro "**Natureza Global**", localizado no menu Ambiente | Parâmetro | TOTVS Gestão Fiscal | 03.03 - Escrituração | Natureza de Operação 1/2 (Etapa 10 - Natureza de Operação da Escrituração Fiscal), o Exercício Fiscal pode ser configurado por Coligada ou por Filial.

Parâmetro

Como o Exercício Fiscal controla a vigência das CFOPs, ele também será afetado por este parâmetro.

parametrosPor Coligada

Quando estiver marcado o campo "**Natureza Global**", as CFOPs ficarão visíveis para todas as Filiais da Coligada, mas não para outras Coligadas.

Neste caso haverá um Exercício Fiscal por Coligada.

Por Filial

Quando estiver desmarcado o campo "**Natureza Global**", cada Filial terá o seu cadastro de CFOP de forma independente.

Neste caso haverá um Exercício Fiscal por Filial, permitindo que cada Filial possa ter a sua máscara independente das demais. Contudo, é um comportamento que deve ser bem avaliado, pois pode dificultar a utilização do TOTVS Gestão Fiscal e futuras manutenções.

# 3. Excluir Exercício Fiscal

O Exercício corrente não poderá ser excluído. Caso deseje excluí-lo, será necessário alterar o contexto do sistema anteriormente, selecionando outro Exercício Fiscal.

# 4. Cadastros afetados pelo Exercício Fiscal

O Exercício Fiscal selecionado no contexto afeta vários cadastros no TOTVS Gestão Fiscal, filtrando-os de acordo com a Data Inicial e Data Final do Exercício.

Exemplos de Cadastros afetados:



Ou seja, quando estes cadastros estiverem fora das datas compreendidas no Exercício Fiscal, eles não serão visualizados pelo usuário independente do filtro que for criado na tela do sistema.

# 5. Definição da Máscara

A Máscara do Código de Natureza deve ser preenchida somente com o caractere "#", e os níveis devem ser definidos com ".".

Exemplo:

| Máscara | CFOP |
| --- | --- |
| #.###.## | 5.102.01 |
| #.###.### | 5.102.001 |
| #.###.##.### | 5.102.01.001 |

Apesar da flexibilidade do cadastro, sempre devem ser observadas as determinações legais deste código, evitando problemas nas entregas das Obrigações Acessórias.

Mesmo com vários níveis definidos no cadastro, as obrigações acessórias só consideram os níveis definidos na legislação. Observando o [Ajuste SINIEF N° 7 DE 28/09/2001](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2001/AJ_007_01) e os exemplos acima, as obrigações serão geradas com o código "5.102".

# 6. Vídeo How To

**648432**

# 7. Exercício Fiscal Default (padrão) no contexto do sistema

Para facilitar a navegação entre as coligadas, ao alterar a coligada selecionada no contexto do sistema, o TOTVS Gestão Fiscal tentará selecionar o Exercício Fiscal vigente para a Coligada, conforme os passos abaixo.

ExercicioDefaulPasso 1

Na tela do assistente de configuração de contexto, poderá ser observado que o Exercício Fiscal estará como "Não preenchido".

Passo 2

Ao acessar o menu do contexto, o Exercício Fiscal estará preenchido.

Para o correto funcionamento deste Default, as regras abaixo devem ser observadas

* O Campo Exercício Fiscal deve estar como "Não Preenchido" na tela do Passo 1;
* Será considerada Data Atual do sistema operacional para localizar um Exercício Vigente;
* A Filial deve estar selecionada no contexto sempre que o parâmetro de "Natureza Global" estiver desmarcado (vide item 2 deste documento).

# 8. Cópia de Exercício Fiscal entre Coligadas

No cadastro de Exercício Fiscal, menu "Processos", está disponível a opção "Cópia de Exercício Fiscal entre Coligadas".

Cópia de Exercício Fiscal entre Coligadas

Este processo é ideal para ser utilizado durante a criação de novas coligadas, mas pode ser usado a qualquer momento em qualquer coligada.

# 9. Outras informações

[Ajuste SINIEF N° 7 DE 28/09/01 altera o Convênio s/n°, de 15.12.70](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2001/AJ_007_01)

```

```

```

```
