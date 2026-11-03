---
content_hash: 2208f51c284df4338d812e6f7225e0a3ea33eba22d9313c957d1af35b9ef4c2e
fetched_at: '2026-06-29T00:08:34.269147+00:00'
page_id: '274656105'
product: rm
source: tdn-rm
title: Gráfico Comparativo INSS Oneração x Desoneração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274656105
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Versões:** | 12.1.13; 12.1.14; 12.1.15; 12.1.16; 12.1.17 |
| **Ocorrência:** | Geração do Gráfico comparativo INSS Oneração x Desoneração |
| **Ambiente:** | Guia de INSS Folha Normal e 13º |
| **Passo a passo:** | Para emitir o gráfico comparativo de INSS Oneração x Desoneração deverá seguir os seguintes passos:  Importar o layout  FOPGRA0002 - Comparativo INSS Oneração x Desoneração    Após importar o Layout do gráfico deverá liberar o acesso para o perfil de usuário      Em "Encargos / Guia de INSS / Parâmetros da Guia de INSS Desoneração" deverá informar para a seção a "Receita Bruta com Desoneração" e "Receita Bruta Demais Atividades" na devida competência para que seja calculado o percentual Redutor. Estes valores serão usados no Gráfico.          O gráfico é acionado na opção Encargos / Guia de INSS / Gráfico comparativo Oneração x Desoneração      O processo de emissão do gráfico solicitará os parâmetros abaixo:  O "% Sobre a Rec. Bruta" se faz necessário para que seja calculado a desoneração que é informada na DARF e que é somado na Desoneração informada na GUIA de INSS.    Receita Bruta: Deverá ser informada a receita bruta, com ela habilitará uma lookup na qual você informará a seção. Caso a receita bruta seja informada o percentual redutor também deverá ser informado.  **Obs: Este processo é manual, na qual para ser feito você deve calcular o "% Redutor" e informar a Receita Bruta. Quando na competência informado não foi informado o percentual redutor devido a competência encontrar-se reonerada.**    Após clicar em Executar deve-se Exibir o relatório:    O Gráfico é mostrado conforme imagem abaixo:  Entenda os cálculos dos valores demostrados.   1. Redutor: **PercentualRedutor  = (ReceitaBrutaDemaisAtividades /( ReceitaBrutaDemaisAtividades + ReceitaBrutaDesoneracao)) \* 100 ou o informado nos parâmetros do processo** 2. Rec. Desonerada: **Receita Bruta \* % Sobre Rec. Bruta / 100 (DARF)** 3. Onerado: **(Base de INSS \* % Empresa) (Autônomo \* % Autônomos)**  Obs: Caso não possua autônomo , o cálculo fica da seguinte maneira **Base de INSS \* % Empresa** 4. Desonerado: **Valor Onerado \* Redutor /100 + Rec.Desonerada** 5. Diferença: **Onerado - Desonerado**     Note que foi incluído dicas sobre outras funcionalidades que o sistema realiza por relatórios. |
| **Observações:** |  |
