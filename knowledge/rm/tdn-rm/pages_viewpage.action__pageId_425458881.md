---
content_hash: 609fb3ba0815426205642a672e19be8292d34bbc9398cabcd5c71e4b0162b071
fetched_at: '2026-06-29T00:09:32.591047+00:00'
page_id: '425458881'
product: rm
source: tdn-rm
title: Registro Acadêmico - R.A
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458881
version: 6
---

Registro Acadêmico (RA) é a identificação do aluno na instituição, ou seja a identidade estudantil do aluno, assim como temos registros que nos identificam na empresa, ou no meio social, como CPF, Título eleitoral, RG, dentre outros.  
    
 Cada instituição pode configurar a máscara para o RA de acordo com sua necessidade, esta pode ter o formato, baseado em algumas informações:  
    
 1.     O R.A pode ser definido para ser calculado por:  
 1.1.   Geral  
 1.2.   Por Curso  
 1.3.   Por Nível de Ensino

Obs. A definição acima é feita na parte de "Secretaria" dos Parâmetros do Educacional.  
    
 2.     Na tabela abaixo mostra o que pode ser utilizado para montar a máscara do R.A.

|  |  |
| --- | --- |
| **Código** | **Descrição** |
| **#** | Números sequenciais |
| **&** | Caracteres do Período Letivo |
| **@** | Digito Verificador Mod. 10 |
| **Letras fixas** | Exceto @,#,& |
| **Números** |  |
| **Separadores** | Ponto, vírgula, barras '/','\',... |

Exemplos:   
 1.     Cálculo de RA "**Geral**" também conhecido como "nenhum"  
 Suponhamos que a instituição queira que seus alunos tenham R.A, baseado em uma Sigla + um sequencial, de forma geral, ou seja todos os alunos seguem a mesma sequência.   
    
 A primeira coisa a fazer é acessar o parametrizador e definir que o cálculo é 'Geral', após feito isso, no próprio parametrizador, deve se informar como será a mascara, neste caso montaremos da seguinte forma a máscara:  TOTVS-#####  
    
 Desta forma, ao cadastrar o primeiro aluno,  o R.A dele será: **TOTVS-00001**, o próximo **TOTVS-00002** e assim por diante.  
    
 2.     Cálculo de RA "**Por Curso**"  
    
 Suponhamos que a instituição queira que seus alunos tenham R.A, baseado em uma Sigla + um sequencial numérico, só que esta sigla seguirá como regra as iniciais de cada curso da instituição.  
    
 A primeira coisa a fazer é acessar o parametrizador e definir que o cálculo será  'Por Curso', em seguida, no [Cadastro de Cursos](http://tdn.totvs.com/x/Af9bGQ), deve se informar como será a máscara para cada um dos cursos da instituição, neste caso montaremos a máscara:  
 Para o curso de Engenharia:   ENG-#####;  
 Para o curso de Direito: DIR-#####  
    
 Assim, os primeiros alunos matriculados receberão o RA formado da sigla definida para o seu curso mais o sequencial.  
    
 3.     Cálculo de RA "**Por Nível de Ensino**"  
    
 Seguindo a mesma idéia do anterior, para o caso do nível de ensino, será definido no parametrizador esta opção e, no [Cadastro de Nível de Ensino](http://tdn.totvs.com/x/2PtbGQ) será definido para cada Nível de Ensino, seguindo nossos exemplos...  
 Ensino Básico:      EB-#####;  
 Ensino Superior:   ES-#####;  
 Pós-Graduação :   POS-#####
